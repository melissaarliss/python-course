operations = ["add", "sub", "mult", "div"]

operation = input("Choose a calculation: add, sub, mult, or div. ").lower().strip()
while operation not in operations:
	operation = input("Try again: the options are add, sub, mult, or div. ").lower().strip()

num_1 = int(input("What is the first number? "))
num_2 = int(input("What is the second number? "))

if operation == "add":
	print(f"The answer is {num_1 + num_2}.")
elif operation == "sub":
	print(f"The answer is {num_1 - num_2}.")
elif operation == "mult":
	print(f"The answer is {num_1 * num_2}.")
elif operation == "div":
	print(f"The answer is {num_1 / num_2}.")		