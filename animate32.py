
import sys
import random

genome_length = random.randint(500, 1500)
read_length = random.randint(50, 150)
num_read = random.randint(50, 200)

#WINDOW INIT
size(1700,500)
background(0)

#GENOME LENGTH GRAPHING
rectMode(CORNERS)
fill(0, 0 , 255)
rect(0, 500, genome_length, 450)
fill(128, 128, 128)

#READ GRAPHING
ntcoverage = []
for i in range(genome_length):
	ntcoverage.append(0)
	stroke(255, 0, 0, 75)
	point(i, num_read)
for i in range(num_read): 
	curreadstart = 0
	curreadstart = random.randint(1, genome_length)
	for j in range(read_length): 
		if curreadstart + j > genome_length:
			break
		else:
			ntcoverage[curreadstart+j-1] += 1
			stroke(255, 0, 0)
			point(curreadstart+j, i)

#COVERAGE GRAPHING
for i in range(len(ntcoverage)):
	stroke(0, 255, 0)
	point(i,400-(ntcoverage[i]*3))
	stroke(0, 128, 0, 75)
	point(i,400)
	point(i,400-max(ntcoverage)*3)

#TEXT IN GRAPH
fill(128, 128, 128)
textSize(20)

text('Reads (n)', genome_length + 50, int(num_read/2))
textSize(10)
text(str(num_read), genome_length + 10, num_read)
textSize(20)

text('Coverage (x)', genome_length + 50, 400 - (max(ntcoverage)*1.5))
textSize(10)
text('0', genome_length + 10, 405)
text(str(max(ntcoverage)), genome_length + 10, 400 - max(ntcoverage)*3)
textSize(20)

text('Genome length (nt)', genome_length + 50, 480)
textSize(10)
text(str(genome_length), genome_length, 445)
text('0', 0, 445)

