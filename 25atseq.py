# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

#---------------------------------------------------------------------------
import random

na = ''
at = 0
atfrac = 0

for i in range(1,31):
	r=random.randint(1,10)
	if r == 1 or r == 2 or r == 3 :
		dna += 'A'
		at += 1
	elif r == 4 or r == 5 or r == 6 :
		dna += 'T'
		at += 1
	elif r == 7 or r == 8:
		dna += 'G'
	elif r == 9 or r ==10:
		dna += 'C'		
	atfrac = at/i
	#print(atfrac) #Checking to see if AT fraction updates every loop
print(len(dna), atfrac, dna)
#---------------------------------------------------------------------------

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
