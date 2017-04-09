# Run search_for_pois.py script
execfile("C:/Users/Bryan/Documents/machine-learning/ud120-projects/datasets_questions/search_for_pois.py")

# Initiate list to hold names of pois
names = []

# Run loop to get names of pois using list from search_for_pois
for k in range(1, number):
	holder = enron_data.keys()[list_pois[k-1]]
	names.append(holder)

# Use names to determine # of pois with NaN for total payments
num_pois_no_pay = 0
for j in range(1, number):
	if enron_data[names[j-1]]["total_payments"] == 'NaN':
		num_pois_no_pay += 1

print num_pois_no_pay