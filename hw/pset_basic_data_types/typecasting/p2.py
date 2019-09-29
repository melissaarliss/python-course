"""
Typcasting w. Strings
"""

# Convert these variables into strings and then back to their original data types. Print out each result as well as its data type. What do you notice about the last one?

five = 5
zero = 0
neg_8 = -8
T = True
F = False

five = str(five)
zero = str(zero)
neg_8 = str(neg_8)
T = str(T)
F = str(F)

# print(five, type(five), zero, type(zero), neg_8, type(neg_8), T, type(T), F, type(F))

five = int(five)
zero = int(zero)
neg_8 = int(neg_8)
T = bool(T)
F = bool(F)

print(five, type(five), zero, type(zero), neg_8, type(neg_8), T, type(T), F, type(F))
