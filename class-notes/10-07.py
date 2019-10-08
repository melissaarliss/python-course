########### FUNCTIONS ################

# def ("define") starts a function

# def function_name(arg1, arg2):
	# action

# call function by writing the function's name	

# Eg:

# def high_low(my_number):
# 	if my_number > 10:
# 		print("high")
# 	else:
# 		print("low")	

# high_low(9)	
# high_low(1/3)
# high_low(-100)	
# high_low(45.67)

##############################################

# def fizz_buzz(num_list):
# 	for num in num_list:
# 		if num%15 == 0:
# 			print("Fizzbuzz")
# 		elif num%3 == 0:
# 			print("Fizz")
# 		elif num%5 == 0:
# 			print("Buzz")
# 		else:
# 			print(num)		

# fizz_buzz(range(1, 21))

##############################################

# def print_order(item):
# 	print(f"Thanks for ordering the {item}!")	

# def order_summ(items_list):
# 	for thing in items_list:
# 		print_order(thing)
# 	print("Your shipping will cost $5.")

# shopping_cart = ["hanging plant", "floor lamp", "toaster", "dream catcher"]

# order_summ(shopping_cart)

##############################################

# def latte_total():
#   price = 5.50
#   sales_tax_rate = .10
#   total_amount = price + (price * sales_tax_rate)
#   print("The total is $", total_amount)

# latte_total()

# def americano_total():
#   price = 4.75
#   sales_tax_rate = .10
#   total_amount = price + (price * sales_tax_rate)
#   print("The total is $", total_amount)

# americano_total()

# def drink_total(drink, price, sales_tax_rate):
# 	total_amount = price + (price * sales_tax_rate)
# 	print(f"You ordered a {drink}. The total amount is ${total_amount}.")
# 	return total_amount

# latte_total = drink_total("latte", 5, .1)

# americano_total = drink_total("americano", 4, .15)

# print(latte_total, americano_total)

##############################################

# def add_two(num):
# 	total = num + 2
# 	print(f"The total is {total}.")
# 	return(total)

# other_total = add_two(4) + 4
# print(other_total)


rainbow = ["red", "orange", "green", "blue", "indigo", "violet"]

print(rainbow)

for i in range(len(rainbow)):
	color = rainbow[i]
	color = len(color)
	print(color)

print(rainbow)





