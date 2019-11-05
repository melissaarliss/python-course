################# SCRIPTING ######################

# "read only" mode with "r" flag - can't write to it
# don't need "r" - it will default to read mode, but nice to have
# my_file = open("hello.txt", "r")
# contents = my_file.read()
# print(contents)
# my_file.close()

# "write only mode" - can't read it
# when you use .write() / "w" mode it will overwrite what's there from a previous operation
# this shows a few different ways to add text
# my_file = open("hello.txt", "w")
# my_file.write("hello world \nhow's it going \n")
# text = ["hi", "hola", "hey"]
# all_text = "\n".join(text)
# my_file.write(all_text)
# my_file.close()

# my_file = open("hello.txt", "r")
# contents = my_file.read()
# print(contents)
# my_file.close()

# another way to access a file
# with open("hello.txt", "w") as my_file:
# 	my_file.write("hi again")
# 	my_file.close()

# with open("hello.txt", "r") as my_file:
# 	contents = my_file.read()
# 	print(contents)
#	my_file.close()

# name = input("What's your name? ")
# food = input("What's your favorite food? ")
# output = f"My name is {name}. My favorite food is {food}."

# with open("about_me.txt", "w") as new_file:
# 	new_file.write(output)
# 	new_file.close()

# with open("about_me.txt", "r") as new_file:
# 	contents = new_file.read()
# 	print(contents)
# 	new_file.close()

####################### PACKAGES AND MODULES ########################

# random is a standard module - don't need to install, just import
import random 

# generate a random int within a certain range
# n = random.randint(5, 105)
# print(n)

# pulls out a random value from a collection
# roygbiv = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# color = random.choice(roygbiv)
# print(color)

# random int from a range - add a 3rd arg for a step
# print(random.randrange(2, 200, 4))

# choose a random float from a range
# x = random.uniform(2, 200)
# print(x)

# return a sample from the given collection with the size given
# sample = random.sample(roygbiv, 3)
# print(sample)

# prints random float between 0.0 and 1.0
# print(random.random())

# all modules are packages but not all packages are modules. packages are larger

# pytime is not a standard packages, needs to be installed with pip
# pytime is a package that contains a module called pytime, so you need to write this syntax
from pytime import pytime

mothers = pytime.mother(1)
print(mothers)

print(pytime.tomorrow())

print(pytime.last_week())



