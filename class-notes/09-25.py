# create a string literal

cupcakes_ive_eaten = 3
# print(cupcakes_ive_eaten)
# print(f"I've eaten {cupcakes_ive_eaten} cupcakes.")

######################

# assignment operators

my_guitars = 3
nikhils_guitars = 1

nikhils_guitars += 2
my_guitars -= 2

# print(f"I have {my_guitars} and Nikhil has {nikhils_guitars}.")

################

# assignment operators and modulo

num1 = 15
num2 = 27

num1 -= num2
num3 = num2 % 2
num1 += 5

# print(num1, num2, num3)

##################

# triple quotes allow you to create a multi line string

fun_string = """
a
b
c
"""

# print(fun_string)

########################

# regular concat

name = 'Marty'
car = 'Delorean'
speed = '88 mph'

# print(f"{name} drove a {car} at a speed of {speed}.")
# print(name, car, speed)
# print(name + " drove a " + car + " at a speed of " + speed + ".")

##########################

# errors

# this won't print, throws a typeerror - can't concat an int and a string
my_num = 5
my_string = 'hello'
# print(my_num + my_string)

#casting - can cast whenever, during printing
num_1 = '10'
num_2 = '20'
print(int(num_1 + num_2))

# or can cast during
my_num1 = '10'
my_num1 = int(my_num1)
my_num2 = '20'
my_num2 = int(my_num2)
# print((my_num1 + my_num2))





