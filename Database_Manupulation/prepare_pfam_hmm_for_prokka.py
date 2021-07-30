"""Add prokka style hmm desc line to Pfam hmms  collection
normal hmm head:
HMMER3/f [3.1b2 | February 2015]
NAME  1-cysPrx_C
ACC   PF10417.10
DESC  C-terminal domain of 1-Cys peroxiredoxin
LENG  40
modify DESC line to rpokka style and add ACC number:
This means PFam accession will placed in the 'gene' column and the product column
"""
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Add DESC line to comncatenated kofam hmm file")
# required arguments
parser.add_argument("-i", "--input", help="Input pFam hmm file", type=str)
parser.add_argument("-o", "--out", help="Output filename (default: pfam-prokka-concat.hmm)", default="ko-prokka-concat.hmm", type=str)

# Parse arguments
args = parser.parse_args()
outfile = args.out
input=args.input


outfile = open(outfile, "w")
previous=None
with open(input, "r") as infile:
    for line in infile:# .readlines():
        previous_line=previous
        previous=line
        if line.startswith("DESC"):
            # get descricption
            desc = line.strip().split("  ")[1]
            acc = previous_line.split()[1]
            new_desc = "DESC  ~~~"+acc+"~~~"+acc+":"+desc+"~~~~~~\n"
            outfile.write(new_desc)
        else:
            outfile.write(line)
        previous = line

outfile.close()