#!/usr/bin/env python3
# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)





#---------------------------------------------------------------------------
import sys
import mcb185
import math

#inputs: [file] [window] [entropy]
#output: [defline] [seq (but changed)]

window = int(sys.argv[2])
entthresh = float(sys.argv[3])
def entropy(seq):
	if len(seq) == 0:
		return (0)
	freq = [0,0,0,0]
	freq[0] = seq.count('A')/len(seq)
	freq[1] = seq.count('C')/len(seq)
	freq[2] = seq.count('G')/len(seq)
	freq[3] = seq.count('T')/len(seq)
	shannon = 0 
	for i in range(len(freq)):
		if freq[i] == 0:
			continue
		shannon = ((freq[i])* math.log2(1/freq[i])) + shannon 
	return(shannon)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	modseq = seq
	for i in range(len(seq)):
		if (entropy(seq[i:i+window])) < entthresh:
			modseq = modseq[:i] + 'N' + modseq[i+1:]
	for i in range(0, len(seq) +180, 61):
		modseq = modseq[:i] + "\n" + modseq[i:]
	print(defline,modseq)
#---------------------------------------------------------------------------
"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
