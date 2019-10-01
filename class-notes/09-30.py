########BOOLEANS#########

# print('derby' < 'apple')

# print('5' == str(5))

# print(5.0 == 5)

# print('5' != 5)

# bool() casts a value as True or False
# 0 / None / empty string prints false, everything else prints true

# to_test = 0
# truthiness = bool(to_test)
# print(f'{to_test} evaluates to {truthiness}.')

# None is the null value in Python

# null_var = None
# print(bool(null_var))



#########CONDITIONALS############################

# indenting is really important in python! actions inside the conditional MUST be indented
# conditionals end in a colon :
# elif = else if
# always need to write the variable name when writing a compound conditions, even if it's the same variable. can wrap them in () for readability.

# temperature = 60.5
# if temperature > 80:
# 	print("It's too hot.")
# elif temperature <= 80 and temperature > 60:
# 	print("It's just right.")	
# elif (temperature <= 60) and (temperature > 40):
# 	print("It's okay.")	
# else:
# 	print("It's too cold.")

# foo = 5
# bar = None
# if foo > 13:
# 	print("Flip")
# elif bar:
# 	print("Flop")
# else:
# 	print("Fly")		

# number = 5
# remainder = number % 2
# if remainder == 0:
# 	print("It's even")
# elif remainder == 1:
# 	print("It's odd")	
# else:
# 	print("It's not an INT")


x = 8
y = 0
a = "Hello!"
b = ""

if x and b:
	print("Both of these are true")
elif bool(y) == False or bool(a) == False:
	print("One of these is false")
elif bool(x) == False or bool(y) == False:
	print("One is false")
	if x > y:
		print("X is greater than Y")
else:
	print("Help")








