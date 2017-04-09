# Find total number of people with NaN for total payments

# create name list
name_list = enron_data.keys()

# use for loop to make list of NaN payment people
no_payments = 0
for i in range(0, 145):
	if enron_data[name_list[i]]["total_payments"] == 'NaN':
		no_payments += 1

print no_payments