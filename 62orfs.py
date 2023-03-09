# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

#---------------------------------------------------------------------------
import argparse
import mcb185
import re

parser = argparse.ArgumentParser(description='Input is file and min ORF size')
parser.add_argument('-f', required=True, type=str, 
	metavar='<str>', help='required, filepath')
parser.add_argument('-o', required=False, type=int, default = 100,
	metavar='<int>', help='minimum ORF length, default is 300nt')
arg = parser.parse_args()


	#translate all the seq and then search for ORFs in those sequences
	#add some +- parameter
for pseqind, seq in mcb185.read_fasta(arg.f):
	orf = {}
	#TURN INTO FXN
	for h in range(3): #gives starts and stops for each frame, value is for aa coord, o
		starts = []
		stops = []
		diff = arg.o
		inseq = mcb185.translate(seq, h)
		peps = inseq.split('*')
		print(peps)
		for match in re.finditer('M\w+\*', inseq):
			print(match.span(), match.group())
			#starts.append(match.start())
		for match in re.finditer('\*', inseq):
			stops.append(match.start())
		i = 0
		j = 0
		currentstart = 0
		while i < len(starts) and j < len(stops):
			if stops[j] - starts[i] >= diff: 
				#threshold met
				#"+ vs - shit"
				print(starts[currentstart]*3 + 1 + h, stops[j]*3 + 3 + h) 
				#catch up to stop
				while starts[i] < stops[j] and i < len(starts)-1: 
					i+=1
				currentstart= i
				i+=1
				j+=1
			elif stops[j] - starts[i] < diff and stops[j] - starts[i] > 0: 
				#not met,retart current start
				#catch up to stop
				while starts[i] < stops[j] and i < len(starts)-1: 
					i+=1
				currentstart= i
				i+=1
			else:
				j+=1

#coordinate sys??:
#				12345			6789
#		+	5'(ACGTACGT)-----------(AAAAAAAA)3'
#		-	3'(AAAAAAAA)-----------(ACGTACGT)5'
#				1....				

#ALTERNATIVE WAY from office hours, something like:
"""
for pseqind, seq in mcb185.read_fasta(arg.f):
	for frame in range(3):
		print(orfs(seq, frame = frame))
"""	
"""
def orfs(seq, frame = 0)
	i = frame
	while i < len(seq):
	codon = seq[i:i+3]
	if codon == 'ATG'
		for j in range(j+3, len(seq),3):
			codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
				if j-i . diff:
					print(i,j)
				i=j
			break
	i+=3
"""
#---------------------------------------------------------------------------
#When printing for the coord, have some '+ window' for modification.
""" OUTPUT IS BIOLOGICAL ANSWER, NEED TO ADD +1 TO START, AND +3 TO END
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW #coordinates here are nt
NC_000913.3 337 2799 + MRVLKFGGTS #frame0 1 lo, 3 lo
NC_000913.3 2801 3733 + MVKVYAPASS #frame1 2 lo, 4 lo
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN #frame1 2 lo, 4 lo
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS #frame0 
"""
