# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax
#---------------------------------------------------------------------------
dna = 'ACTGAAAAAAAAAAA'


dna = dna[::-1]

print(dna)








































"""


andy = ''	
for nt in range(len(dna)):
	if dna[nt] == 'A':
		andy = andy[:(len(andy))-nt] + 'T' + andy[(len(andy))-nt:] 
		print(andy)
	elif dna[nt] == 'C':
		andy = andy[:(len(andy))-nt] + 'G' + andy[(len(andy))-nt:] 
		print(andy)
	elif dna[nt] == 'G':
		andy = andy[:(len(andy))-nt] + 'C' + andy[(len(andy))-nt:] 
		print(andy)
	elif dna[nt] == 'T':
		andy = andy[:(len(andy))-nt] + 'A' + andy[(len(andy))-nt:] 
		print(andy)
print(andy)

#Or just reverse a string some other way
"""
#---------------------------------------------------------------------------
"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
