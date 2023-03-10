# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
#---------------------------------------------------------------------------
import math
import sys

#Create list given command line input
Shan_list = []

for val in sys.argv[1:]:
	Shan_list.append(float(val))

#stop incorrect input
assert(math.isclose(sum(Shan_list), 1.0)) #Input doesn't equal 1

#calculate H
shannon = 0 

for i in range(len(Shan_list)):
	shannon = ((Shan_list[i])* math.log2(1/Shan_list[i])) + shannon 
print(f'{shannon:.3f}')
#---------------------------------------------------------------------------

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
