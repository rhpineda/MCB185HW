# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator
#---------------------------------------------------------------------------
dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for i in range(0,len(dna),3):
	print(dna[i:i+3])

#for nt in range(0,len(dna),3):
#	codon = dna[nt:nt+3]
#	print(codon)
#---------------------------------------------------------------------------
"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
