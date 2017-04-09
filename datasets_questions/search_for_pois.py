# Impore enron data
# Note: poi stands for person of interest
execfile("C:/Users/Bryan/Documents/machine-learning/ud120-projects/datasets_questions/explore_enron_data.py")

# Initiate i as while loop counter
# use number to count number of people with feature
i = 0
number = 0
list_pois = []

# Use while loop to check if for feature
# for each of the 146 people and count total
while i < 146:
	if enron_data.values()[i].values()[15] == True:
		number += 1
		list_pois.append(i)
	i += 1

# Print answer for total number of features
print number
