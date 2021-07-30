import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Add DESC line to comncatenated kofam hmm file")
# required arguments
parser.add_argument("-i", "--input", help="Input file with counts and length column fromfeatureCounts" , type=str)
parser.add_argument("-o", "--out", help="Output file bas name", type=str)

# Parse arguments
args = parser.parse_args()
outbase = args.out
input=args.input
outtpm = outbase + "_TPM.tsv"
outcount = outbase + "_NumReads.tsv"

def calculate_RPK(count, gene_length):
    # divide count by gene length in kB
    return count / (gene_length/1000)

def calculate_TPM(RPK, summedRPK):
    # sum up all RPK values and divide by 1 Mio, that is the scaling factor
    return round(RPK / (summedRPK /10**6), 3)


def main():
    # read input table
    df = pd.read_csv(input, sep="\t", skiprows=1)
    df = df.drop(["Chr", "Start","End","Strand"],axis=1).set_index(["Geneid"])
    df_counts = df
    gene_lengths = df["Length"]
    # calulate RPK
    df = df.iloc[:,1:].div(gene_lengths, axis=0)
    # scale to TPM
    df_tpm = round(df[df.columns].div(df[df.columns].sum() / 10**6, axis=1),5)

    # write output
    df_tpm.to_csv(outtpm, sep="\t")
    df_counts.to_csv(outcount, sep="\t")
if __name__ == "__main__":
    # execute only if run as a script
    main()