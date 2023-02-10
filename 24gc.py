# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

#---------------------------------------------------------------------------
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

gccounter = 0

for i in range(0,len(dna)): #dna[i] is equal to going over each nt
	if dna[i] == 'C' or dna[i] == 'G':
		gccounter = gccounter + 1

print(f'{gccounter/len(dna):.2f}')
#---------------------------------------------------------------------------
"""
python3 24gc.py
0.42
"""
