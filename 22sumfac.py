# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

#---------------------------------------------------------------------------
n = 5
sum = 0
fac = 1
for i in range(n):
	sum += (i+1)
	fac = (i+1)*fac
print(n)
print(sum)
print(fac)
#---------------------------------------------------------------------------

"""
python3 22sumfac.py
5 15 120
"""
