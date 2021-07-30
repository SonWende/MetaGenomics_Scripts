from Bio import SeqIO
import pandas as pd
import argparse
import sys
import seaborn as sns
from matplotlib.patches import Rectangle

"""Plot a histogram of sequence length distributions for a mulitfasta file
"""

#TODO: finish hist plot output

# Matplotlib #
import matplotlib
#matplotlib.use('Agg', warn=False)
from matplotlib import pyplot

################################################################################

parser = argparse.ArgumentParser(description="Plot a histogram of sequence length distribution for a mulitfasta file")
# required arguments
parser.add_argument("-i", "--input", help="Input multifasta file to process", type=str)#, required=True)
parser.add_argument("-o", "--out", help="Plot output filename (default: seq-length-histogram.png)", default="seq-length-histogram.png", type=str)
# optional arguments
parser.add_argument("--log", help="Logscale of y-axis (default: True)", default=False, type=bool)
parser.add_argument("--bins", help="Set number of bins (default: 100)", default=100, type=int)
# Parse arguments
args = parser.parse_args()
output_path = args.out
file="consolidated.fasta"
#file=args.input
################################################################################
# Read file ent get sequence lengths
lengths = map(len, SeqIO.parse(file, 'fasta'))
values = pd.Series(lengths)
# Report to command line
sys.stderr.write("Number of sequences: %i \n" % len(values))
sys.stderr.write("Shortest sequence: %i bp\n" % values.min())
sys.stderr.write("Longest sequence: %i bp\n" % values.max())
sys.stderr.write("Making graph...\n")
textbox = "Number of seqs: " + str(len(values))+ "\nShortest seq: " + str(values.min()) + "\nLongest seq: " + str(values.max())
title = 'Distribution of sequence lengths'
ax = values.hist(color='gray', bins=args.bins, label=textbox)
ax.set(title="Contig Length Distribution Histogram")
ax.legend()

ax.set(xlabel='contig lengths (bp)')
ax.set(ylabel='Density')


#ax = sns.distplot(values, hist = False, kde = True,kde_kws = {'linewidth': 3})
#ax.set(xlabel='contig lengths (Kb)')

fig = ax.get_figure()
# Save it #
fig.savefig(output_path)