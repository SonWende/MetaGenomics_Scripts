#!/usr/bin/env python
''' Filter blast or diamond tabular output for best hits

This scripts filters blast tabular output for the best hit based on bitscore, percent match length and percent identity and evalue
Input parameters:
    - tabular blast input file
        Blast and diamond need to be run with the following output format specifications:
        --outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen slen"
    - percent_match_length to filter for (percent match length is calculated from alen /qlen) (percent of query aligned)
    - evalue threshold to filter for
    - percent identity to filter for
    -

This script requires the following packages:
- argparse
- pandas


'''
#TODO: everything!!
import argparse



def best_bistscore():
    """For given query, filter hit results based on highest bitscore"""
