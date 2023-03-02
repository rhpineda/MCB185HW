#!/usr/bin/env python3
# 50dust.py
#---------------------------------------------------------------------------
# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters


# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

#---------------------------------------------------------------------------

import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description= \
	'Change middle nt in window if low entropy')
parser.add_argument('-w', required=False, type=int, default=11,
	metavar='<int>', help='"word length used", default is: [%(default)i]')
	
parser.add_argument('-t', required=False, type=float, default=1.4,
	metavar='<float>', help='"entropy threshold", default is: [%(default)f]')
	
parser.add_argument('-s',required=True, type=str, 
	metavar='<str>', help='file/string to evaluate')
	
parser.add_argument('-n', required=False, action='store_true',
	help='N-based or soft masking')

arg = parser.parse_args()
window = int(arg.w)
entthresh = float(arg.t)

def entropy(seq):
	if len(seq) == 0:
		return (0)
	freq = [0,0,0,0]
	freq[0] = seq.count('A')/len(seq)  + seq.count('a')/len(seq)
	freq[1] = seq.count('C')/len(seq)  + seq.count('c')/len(seq)
	freq[2] = seq.count('G')/len(seq)  + seq.count('g')/len(seq)
	freq[3] = seq.count('T')/len(seq)  + seq.count('t')/len(seq)
	shannon = 0 
	for i in range(len(freq)):
		if freq[i] == 0:
			continue
		shannon = ((freq[i])* math.log2(1/freq[i])) + shannon 
	return(shannon)

for defline, seq in mcb185.read_fasta(arg.s):
	seq = seq.upper()
	mods = seq 
	midwin = int(window/2)
	for i in range((midwin), len(seq) - midwin) : 
		if entropy(seq[i-midwin:i+midwin+1]) < entthresh:
			if arg.n == True:
				msk = 'N'
			else: 
				msk = seq[i].lower()
			for j in range(i-midwin, i+midwin+1):
				mods = mods[:j] + seq[j].lower() + mods[j+1:]		
	
	for i in range(0, len(mods) + int(len(mods)/60) , 61):
		mods = mods[:i] + "\n" + mods[i:]
	print('>' + defline, mods)

#---------------------------------------------------------------------------
"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
