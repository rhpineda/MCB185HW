# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys
#---------------------------------------------------------------------------
import sys

#Create list
Num_list = []

for val in sys.argv[1:]:
	Num_list.append(float(val))
	
#Do math for SD
Mean = sum(Num_list)/len(Num_list) #Easier to work with for solving SD
SD = 0

for i in range(len(Num_list)):
	SD = (Num_list[i] - Mean) ** 2/(len(Num_list)) + SD
SD = SD ** 0.5

#Do math for Median
Num_list.sort()

if len(Num_list) % 2 == 0: #If list of numbers is even
	Median = (Num_list[(int(len(Num_list)/2))-1] + \
		Num_list[int(len(Num_list)/2)]) / 2
else: # if list of numbers isn't even
	Median = (Num_list[(int(len(Num_list)/2))])

#Printing desired values
print('Count:', len(Num_list))
print('Minimum:', min(Num_list))
print('Maximum:', max(Num_list))
print('Mean:', f'{Mean:.3f}')
print('Std. dev.:', f'{SD:.3f}')
print('Median:'f'{Median:.3f}')

#---------------------------------------------------------------------------
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
