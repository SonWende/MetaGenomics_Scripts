import random
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys


"""For given multifasta file, randomly mutate sequences to error rate
Randomly aplly point mutations, insertions, deletions
"""

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def deletion(s, position):
    return replace_str_index(s, position, "")


def insertion(s, position):
    curr = s[position]
    ins = random.choice([x for x in "ACTG"])
    insert = ''.join([curr, ins])
    return replace_str_index(s, position, insert)


def mutation(s, position):
    curr = s[position]
    return replace_str_index(s, position, random.choice([x for x in "ACTG".replace(curr.upper(), "")]))


def main(args):
    with open(args.input) as handle, open(args.output, 'w') as output:
        # gather function in list
        mutation_freq = float(args.frequency)
        functions = [deletion, insertion, mutation]
        # read sequences
        for record in SeqIO.parse(handle, "fasta"):
            # get current sequence
            seq = record.seq
            # get length of sequence:
            seqLen = len(seq)
            # pick number of mutations to perform
            num_mutations = int(seqLen * mutation_freq)
            # generate random list of position to mutate
            rand_mut_positions = [random.randint(0, seqLen- num_mutations) for m in range(0, num_mutations)]
            # randomly apply insertion, deletion or mutation to selected positions
            for m in rand_mut_positions:
                seq = random.choice(functions)(seq, m)
            newrecord = SeqRecord(Seq(seq), id = record.id)
            SeqIO.write(newrecord, output, "fasta")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = __doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', '--input',
            help="(multi)fasta file as input")
    parser.add_argument('-o', '--output',
                        help="output file name")
    parser.add_argument('-f', '--frequency',
                        help="mutation rate (0.01 for 1%")
    args = parser.parse_args()
    main(args)

