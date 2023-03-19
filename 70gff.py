# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

#---------------------------------------------------------------------------
import json
import re
import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
	allgene = []
	genedict = {}
	for line in fp.readlines(): 
		gene =  re.search('gbkey=Gene;gene=([^;]*)' , line)
		tempdict = {}
		if gene:
			pos = re.search('(\d+)\s(\d+)' , line)
			strand = re.search('(?<=\t)[+-](?=\t)', line)
			tempdict = {'gene':gene.group(1), 'beg':pos.group(1),\
						'end':pos.group(2), 'strand':strand.group(0)}
			allgene.append(tempdict)
print(json.dumps(allgene, indent=4))

#------------------------------------------------------------------------
"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
