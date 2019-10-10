#### NESTED LISTS

coordinates = [
	[0,5],
	[1,4],
	[-3,2]
]

# prints the list at this index
# print(coordinates[0])

# goes to the list at index 0 and finds the item at index 1
# print(coordinates[0][0])

# test = coordinates[0]
# a = test[0]
# b = test[1]
# c = (a**2 + b**2)**(1/2)
# print(c)

# def calculate_distance(x, y):
# 	return (x**2 + y**2)**(1/2)

# print(calculate_distance(1,4))

# prints both items in the nested list on their own, not in a list
for x, y in coordinates:
	print(x, y)

# prints the entire list element
# for xy_pair in coordinates:
# 	x = xy_pair[0]
# 	y = xy_pair[1]
# 	print(x, y)

# for x, y in coordinates:
# 	distance = calculate_distance(x, y)
# 	distance = round(distance, 2)
# 	print(f"Coordinates {x} and {y} are {distance} away.")



