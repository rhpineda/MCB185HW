# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

#---------------------------------------------------------------------------

import sys
import random

# input is : genome_length, read_length, num_read
#Convert input to variables
genome_length = int(sys.argv[1])
read_length = int(sys.argv[2])
num_read = int(sys.argv[3])

#Genome list becomes list of nt of genome_length
genome_list = []

for i in range(genome_length): 
	addnt = random.choice('ACGT')
	genome_list.append(str(addnt))

#nt coverage becomes list of coverage of given
ntcoverage = []
visualizecoverage = []
for i in range(genome_length):
	ntcoverage.append(0)
	visualizecoverage.append('')
for i in range(num_read): 
	curreadstart = 0
	curreadstart = random.randint(1, genome_length)
	for j in range(read_length): 
		if curreadstart + j > genome_length:
			break
		else:
			ntcoverage[curreadstart+j-1] += 1
			(visualizecoverage[curreadstart+j-1]) += '|'


#Visualize covarage dist (column view)
for a, b in zip(visualizecoverage, genome_list):
	print (b, a)

#Visualize covarage dist (row view)
#print(ntcoverage)
#print(genome_list)


print('^^^^COVERAGE VISUALIZED^^^^')
#Print min max, and raw avg
print('EDGES INCLUDED')
print('MIN',min(ntcoverage), \
	'MAX', max(ntcoverage), \
	'AVG', (sum(ntcoverage)/genome_length))

#Accounting for edge effects
firstedgelessnt	= ntcoverage[read_length:]

print('FIRST EDGE NOT INCLUDED')
print('MIN', min(ntcoverage), \
	'MAX',max(ntcoverage),\
	'AVERAGE', (sum(firstedgelessnt)/((genome_length)-(read_length))))

#Accounting for edge effects
edgelessnt	= ntcoverage[read_length:genome_length-read_length]

print('BOTH EDGES NOT INCLUDED')
print('MIN', min(ntcoverage), \
	'MAX',max(ntcoverage),\
	'AVERAGE', (sum(edgelessnt)/((genome_length)-(2*read_length))))
#---------------------------------------------------------------------------
#SAMPLE OUTPUT
"""
rick@rick-VirtualBox:~/Code/MCB185HW$ python3 32xcoverage.py 20 5 200
A ||||||||||
G ||||||||||||||||||
C ||||||||||||||||||||||||||||||
C ||||||||||||||||||||||||||||||||||||||||||||
T ||||||||||||||||||||||||||||||||||||||||||||||||||||||
G ||||||||||||||||||||||||||||||||||||||||||||||||||||||
C |||||||||||||||||||||||||||||||||||||||||||||||||||
T ||||||||||||||||||||||||||||||||||||||||||||||||
A ||||||||||||||||||||||||||||||||||||||||||||||||||
T |||||||||||||||||||||||||||||||||||||||||||||||||||||
T ||||||||||||||||||||||||||||||||||||||||||||||||||||
C ||||||||||||||||||||||||||||||||||||||||||||||||||||||
A ||||||||||||||||||||||||||||||||||||||||||||||||||||
A ||||||||||||||||||||||||||||||||||||||||||||||
T ||||||||||||||||||||||||||||||||||||||||
T ||||||||||||||||||||||||||||||||||||||
A |||||||||||||||||||||||||||||||||||||||||||||||
C |||||||||||||||||||||||||||||||||||||||||||||||||||
G ||||||||||||||||||||||||||||||||||||||||||||||||||||
A |||||||||||||||||||||||||||||||||||||||||||||||||||||
^^^^COVERAGE VISUALIZED^^^^
EDGES INCLUDED
MIN 10 MAX 54 AVG 44.85
FIRST EDGE NOT INCLUDED
MIN 10 MAX 54 AVERAGE 49.4
BOTH EDGES NOT INCLUDED
MIN 10 MAX 54 AVERAGE 50.0

"""
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
