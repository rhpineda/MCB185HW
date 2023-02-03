# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
#---------------------------------------------------------------------------

import random
import sys

#Input -> variables
year_length = int(sys.argv[1])
num_ppl = int(sys.argv[2])
#num_simulations = int(sys.argv[3])


#Intialize counter and test container of duplicate birthdays
repeatbirth = 0
repeatbirthcount = False

for h in range(1000): #LOOP for amt of simul
#initialize empty year list to add birhtdays to
	year_list = []
	for i in range(year_length):
		year_list.append(0)
	for i in range(num_ppl): #LOOP for adding birthdays to a list
		addperson = 0
		addperson = random.randint(1, year_length)
		#print(addperson) #shows the birthday of the new person being added
		year_list[addperson-1] += 1
		if year_list[addperson-1] > 1: #Tests if simulation has a repeat
			repeatbirthcount = True
		else:
			continue
	if repeatbirthcount == True: 
		repeatbirth += 1		 #increases the number of repeat simulations
		repeatbirthcount = False #resets the test if simulation is a repeat
		year_list = []
	else:
		continue
print('PROPORTION OF SIMULATIONS WITH A REPEAT BIRHTDAY IN 1000 SIMULATIONS')
print(repeatbirth/1000)


#---------------------------------------------------------------------------

"""
python3 33birthday.py 365 23
0.571
"""

