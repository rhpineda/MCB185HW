# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

#---------------------------------------------------------------------------

import mcb185
import argparse

parser = argparse.ArgumentParser(description='Input is file and k')
parser.add_argument('-f', required=True, type=str, 
	metavar='<str>', help='required, filepath')
parser.add_argument('-k', required=False, type=int, default = 1,
	metavar='<int>', help='k, default is 1')
arg = parser.parse_args()

#find and calc totals of the kmers in a seq
filename = arg.f
k = arg.k

kmerdict = {}
totalkmer = 0
for defline, seq in mcb185.read_fasta(arg.f):
	for i in range(len(seq)-k-1):
		newkmer = seq[i:i+k]
		if newkmer not in kmerdict:
			kmerdict[newkmer] = 0
		kmerdict[newkmer] += 1
		totalkmer += 1

#print in desired format
for keykmer, totalvalkmer in sorted(kmerdict.items()):
	print(keykmer, totalvalkmer)



#---------------------------------------------------------------------------
"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
