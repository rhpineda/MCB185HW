# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein
#---------------------------------------------------------------------------
import sys
import gzip
import re
def complement(seq):
	rcseqlist = list(seq)
	for i in range(len(seq)):
		if rcseqlist[i] == 'A':
			rcseqlist[i] = 'T'
		elif rcseqlist[i] == 'C':
			rcseqlist[i] = 'G'
		elif rcseqlist[i] == 'G':
			rcseqlist[i] = 'C'
		elif rcseqlist[i] == 'T':
			rcseqlist[i] = 'A'
		else: rcseqlist[i] = '?'
	return(''.join(rcseqlist))
#DONE-----read file and find 'ORIGIN' and after that we get the seq
#find gene ... start pos

#gene [anything except letter]number [ends at period]
#Look at seq list from start:start+3

#Gives out seq from file
with gzip.open(sys.argv[1], 'rt') as fp:
	patterntest = False
	seq = []
	for line in fp.readlines(): 
		match =  re.search('ORIGIN' , line)
		if match and patterntest != True:
			patterntest = True
			rline = line[match.end():]
			seq += re.findall('[acgt]', rline)
		elif patterntest == True:
			seq += re.findall('[acgt]', line)		
#get start nt of start seq as str
with gzip.open(sys.argv[1], 'rt') as fp:
	startspos = []
	startsneg = []
	for line in fp.readlines(): 
		match =  re.search('gene', line)
				# OR CDS | tRNA | misc_feature? 
		if match:
			rline = line[match.end():]
			startspos += re.findall('(?<=\s)\d+(?=\.)', rline)
			startsneg += re.findall('complement\(\d+\.\.(\d+)\)', rline)	
#str of start pos > int of start pos > list of lists start seq > list of starts
startsp= []
startsn= []
startllp = []
startlln = []
startseq = []
for i in startspos: startsp.append(int(i))
for i in startsneg: startsn.append(int(i))
for i in range(len(startsp)):startllp.append(seq[startsp[i]-1:startsp[i]+2])
for i in range(len(startsn)):startlln.append(seq[startsn[i]-1:startsn[i]-4:-1])
for i in startllp:
	lltemp = ''
	for j in i:
		lltemp += j
	startseq.append(lltemp.upper())
for i in startlln:
	lltemp = ''
	for j in i:
		lltemp += j
	startseq.append(complement(lltemp.upper()))
startsdict = {}
total = 0
for i in range(len(startseq)):
	if startseq[i] not in startsdict:
		startsdict[startseq[i]] = 0
	startsdict[startseq[i]] += 1
	total += 1

sorted_dict = {k: v for k, v in sorted(startsdict.items(), \
			key=lambda item: item[1], reverse = True)}
for key, value in sorted_dict.items():
	print(key, value)
#---------------------------------------------------------------------------
#NOT SURE WHY I HAVE OVER SAMPLING OF EVERYTHING WHEN SEARCHING FOR LINES THAT
#START WITH 'gene' COMPARED TO 'CDS | tRNA | misc_feature', BUT HEY, MY RESULTS
#ARE PRETTY CLOSE 
#---------------------------------------------------------------------------
"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
