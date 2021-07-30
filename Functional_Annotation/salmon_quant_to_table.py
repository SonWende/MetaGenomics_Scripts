import pandas as pd
import argparse
from functools import reduce
from glob import glob

parser = argparse.ArgumentParser(description="Add DESC line to comncatenated kofam hmm file")
# required arguments
parser.add_argument("-i", "--files", help="Input files (quant.sf files) from salmon quantification" , nargs="*", type=str)
parser.add_argument("-o", "--out", help="Output file base name", type=str)
parser.add_argument("--clean", type="str", help="regex to clean from sample name", required=False)

# parse files from wildcard
files = []
args = parser.parse_args()
for arg in args.files:
    files += glob(arg)
outbase = args.out
outcount = outbase + "_NumReads.tsv"
outtpm = outbase + "_TPM.tsv"
dfs=[]

def main():
    dfs = []
    for f in files:
        df = pd.read_csv(f, sep="\t")
        name = f.split("/")[-2]
        if args.clean is not None:
            name = name.replace(args.clean, "")
        print(name)
        #name = name.replace("/quant.sf", "")
        df = df.rename(columns={"TPM": "TPM_" + name, "NumReads": "NumReads_" + name})
        dfs.append(df)
    df = reduce(lambda df1, df2: pd.merge(df1, df2, on='Name'), dfs)
    df = df.set_index("Name")

    df.filter(regex="NumReads_").to_csv(outcount, sep="\t")
    df.filter(regex="TPM_").to_csv(outtpm, sep="\t")
    # df.filter(regex="NumReads_t").to_csv("salmon_quant_NumReads_combined_metagenomes_prokka.ffn.tsv", sep="\t")
    # df.filter(regex="TPM_t").to_csv("salmon_quant_TPM_combined_metagenomes_prokka.ffn.tsv", sep="\t")

if __name__ == "__main__":
    # execute only if run as a script
    main()