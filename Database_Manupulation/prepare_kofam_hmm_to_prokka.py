"""for given KO hmms (concatenated) add a prokka style DESC line to the hmms
parse file: after line
NAME    K00001
insert prokka syle DESC line, look up information from kolist
DESC line hast the formatting EC~~~KOnumber~~~KOnumber:description~~~empty~~~
This means KOnumber will be placed in the 'gene' column and the product column"""


import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Add DESC line to comncatenated kofam hmm file")
# required arguments
parser.add_argument("-i", "--input", help="Input concatenated ko hmm", type=str)
parser.add_argument("-k", "--kolist", help="KO list file with Knum information", type=str)
parser.add_argument("-o", "--out", help="Output filename (default: ko-prokka-concat.hmm)", default="ko-prokka-concat.hmm", type=str)

# Parse arguments
args = parser.parse_args()
outfile = args.out

kolist=pd.read_csv(args.kolist, sep="\t", usecols=["knum", "definition"])
kolist["EC"] = kolist["definition"].apply(lambda st: st[st.find("[EC")+4:st.find("]")] if "[EC" in st else "")
print(kolist.tail())

outfile = open(outfile, "w")
with open(args.input, "r") as infile:
    for line in infile.readlines():
        if line.startswith("NAME"):
            # get KOnumber
            knum = line.split()[1]
            # get DES line for KONumber
            row = kolist.loc[kolist["knum"]==knum]
            print(row.iloc[0,2])
            desc= "DESC  "+row.iloc[0,2]+"~~~"+knum+"~~~"+knum+":"+row.iloc[0,1]+"~~~~~~\n"
            line=line+desc
            outfile.write(str(line))
            #print(line)
        else:
            outfile.write(line)

outfile.close()