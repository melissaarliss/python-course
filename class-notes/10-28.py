################# SCOPE ##################

# def my_func1():
# 	x=1
# 	print(x)


# can have another local x variable in this function since its local
# def my_func2():
# 	x=2
# 	print(x)

# print(x) # this will error since x is local not global

########################

# def cool_func():
# 	bar = 8
	# return bar

# bar is local, won't return if return is commented out
# print(bar)

# x = cool_func() 		
# print(x) # this will return bar / 8, but if the function didn't return anything it wouldn't work

###################

# foo = 5

# won't run because foo is in global - we can find and read things in global scope but can't affect it d 
# def increment_foo():
# 	foo += 1
# 	return foo
# 	print(foo)

# print(foo)
# print(increment_foo())

# this will run if we pass the global variable in in
# def increment_foo(foo):
# 	foo += 1
# 	print(foo)
# 	return foo

# foo will be the same, still 5
# print(foo)

# now foo will be reassigned from the function
# foo = increment_foo(foo)

###############################

# this allows us to read and write to the global variable from inside the function - add the global keyword before the variable name
# def increment_foo():
# 	global foo
# 	foo += 1
# 	print(foo)
# 	return foo

# print(foo)
# increment_foo()	

############

# piranhas_hungry = True

# def swing_vine_over_river():
# 	global piranhas_hungry
# 	print("Piranhas got me!")
# 	piranhas_hungry = False

# def jump_in_river():
# 	if piranhas_hungry:
# 		print("I'm not going in there! The piranhas are hungry")
# 	else:
# 		print("Swimming happily down the river, the piranhas are full")	

# jump_in_river()
# swing_vine_over_river()
# jump_in_river()

######################### DEBUGGING ############################

# my_favorites = {
# 	"Food": "Lobster Rolls",
# 	"Song": "Bohemian Rhapsody",
# 	"Flower": "Iris",
# 	"Band": "Tom Petty & the Heartbreakers",
# 	"Color": "Green",
# 	"Movie": "The Princess Bride",
# 	"Programming Language": "Python"
# }

# this doesn't work - key doesn't exist
# print("My favorite restaurant is", my_favorites["Restaurant"])

# fix this using an if statement
# if "Restaurant" in my_favorites:
# 	print("My favorite restaurant is", my_favorites["Restaurant"])
# else:
# 	my_favorites["Restaurant"] = "Pizza Hut"	

# print("My favorite restaurant is", my_favorites["Restaurant"])

###################

# try-except blocks
# differs from if-else bc both lines will always run

# my_num = None

# while my_num is None:
# 	try:
# 		my_num = int(input("Give me a number: "))
# 	except ValueError as err:
# 		print("Try again, that doesn't work")
# 		print("Error was ", err)

# print("Thanks for playing")

################

# import pdb

# pdb.set_trace() allows you to stop it from running at a certain point in the program (wherever you put it)
# def func1(my_list):
# 	for num in my_list:
# 		pdb.set_trace()
# 		print(num)
# 	if num % 2 == 0:
# 		print(num)

# func1([1,2,3,4,5])			

############

class Phone:
	def __init__(self, phone_number=0):
		self.number = phone_number

	def call(self, other_number):
		print("Calling from", self.number, "to", other_number)

	def text(self, other_number, msg):
		print("Sending text from", self.number, "to", other_number)
		print(msg)

new_phone = Phone(5214)
test_phone = Phone()
test_phone.call(515)
test_phone.text(int("141"), "Hi!")





