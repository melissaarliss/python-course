operations = ["add", "sub", "mult", "div"]

operation = input("Choose a calculation: add, sub, mult, or div. ").lower().strip()
while operation not in operations:
	operation = input("Try again: the options are add, sub, mult, or div. ").lower().strip()

num_1 = int(input("What is the first number? "))
num_2 = int(input("What is the second number? "))

if operation == "add":
	answer = num_1 + num_2
elif operation == "sub":
	answer = num_1 - num_2
elif operation == "mult":
	answer = num_1 * num_2
elif operation == "div":
	answer = num_1 / num_2

print(f"The answer is {answer}.")		