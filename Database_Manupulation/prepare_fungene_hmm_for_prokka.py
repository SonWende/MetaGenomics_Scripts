"""HMMER3/f [3.3 | Nov 2019]
NAME  nirB
DESC  nirB
LENG  847
ALPH  amino

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
            acc = line.strip().split("  ")[1]
            new_desc = "DESC  ~~~"+acc+"~~~"+acc+":fungene"+"~~~~~~\n"
            outfile.write(new_desc)
        else:
            outfile.write(line)
        previous = line

outfile.close()