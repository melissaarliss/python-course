def multiply(num, num_list):
	for i in range(len(num_list)):
		num_list[i] = num_list[i] * num
	return num_list

print(multiply(3, [4,5,6]))