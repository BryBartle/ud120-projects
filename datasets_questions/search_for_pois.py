# Impore enron data
# Note: poi stands for person of interest
execfile("C:/Users/Bryan/Documents/machine-learning/ud120-projects/datasets_questions/explore_enron_data.py")

# Initiate i as while loop counter
# use number of pois as number of pois counter 
i = 0
number_of_pois = 0

# Use while loop to check if poi is False or True
# for each of the 146 people and count total
while i < 146:
	if enron_data.values()[i].values()[15] == True:
		number_of_pois += 1
	i += 1

# Print answer for total number of pois
print number_of_pois
