

import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import argparse

parser = argparse.ArgumentParser(description="Add DESC line to comncatenated kofam hmm file")
# required arguments
parser.add_argument("-txt", "--input", help="Input concatenated ko hmm", type=str)
parser.add_argument("-k", "--kolist", help="KO list file with Knum information", type=str)
parser.add_argument("-o", "--out", help="Output filename (default: ko-prokka-concat.hmm)", default="ko-prokka-concat.hmm", type=str)

# Parse arguments
args = parser.parse_args()
outfile = args.out
# Use the venn2 function
venn2(subsets = (10, 5, 2), set_labels = ('Group A', 'Group B'))
plt.show()