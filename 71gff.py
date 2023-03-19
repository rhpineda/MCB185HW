# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file
#---------------------------------------------------------------------------

import gzip
import sys
import re
import json

with gzip.open(sys.argv[1], 'rt') as fp:
	alldict = {}
	tempchromosomelist = []
	for line in fp.readlines(): 
		gene =  re.search('sequence_name=([^;]*)' , line)
		chromosome = re.search('^([^\t]+)', line)
		tempdict = {}
		if gene:
			if chromosome.group(1) not in alldict:
				tempchromosomelist = []
			pos = re.search('(\d+)\s(\d+)' , line)
			strand = re.search('(?<=\t)[+-](?=\t)', line)
			tempdict = {'gene':gene.group(1), 'beg':int(pos.group(1)),\
						'end':int(pos.group(2)), 'strand':strand.group(0)}
			alldict[chromosome.group(1)] = tempchromosomelist
			tempchromosomelist.append(tempdict)

for key in alldict:
    print(key, len(alldict[key]))
print(json.dumps(alldict, indent=4))
#---------------------------------------------------------------------------
"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
