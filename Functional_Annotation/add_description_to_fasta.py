from Bio import SeqIO
from itertools import islice
import pandas as pd

infile = "D:\\ABreidenbach\\Metagenome\\Annotation_Results_Prokka\\PROKKA_06112021.faa"
mapfile = "D:\\ABreidenbach\\Metagenome\\Annotation_Results_Prokka\\rname_additional_annotations.txt"
outfile = "D:\\ABreidenbach\\Metagenome\\Annotation_Results_Prokka\\PROKKA_06112021.renamed.faa"
map = pd.read_csv(mapfile, sep="\t", names=["id", "desc"])
map = pd.Series(map.desc.values, index=map.id).to_dict()

print(map)
with open(infile) as fastain, open(outfile, 'w') as out:
    records = SeqIO.parse(fastain, "fasta")
    for record in records:
        if record.id in map.keys():
            # new header
            #newheader = record.id + " " + map[record.id]
            record.description =  map[record.id]
        SeqIO.write(record, out, "fasta")
            #print(newheader)
"""

infile = "D:\\ABreidenbach\\Metagenome\\Annotation_Results_Prokka\\PROKKA_06112021.renamed.faa"
with open(infile) as fastain:
    records = SeqIO.parse(fastain, "fasta")
    for record in islice(records, 20):
        print(record.id)
        print(record.description)
"""