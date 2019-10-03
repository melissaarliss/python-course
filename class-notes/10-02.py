########CONDITIONALS PRACTICE#############

# val1 = True == (not False)
# print(val1)

# val2 = not 0
# print(val2)

# val3 = (7 == "7") or (not "")
# print(val3)

# a_string = "hey"
# val4 = len(a_string) > -1**2
# print(val4)

#########LISTS###########

# lists hold multiple items of any data type
# 0 indexed, ordered
# noted with square brackets []

# get the length of a list with len(list_name)
# students = ["Sandy", "Ian", "Bersys"]
# print(len(students))
# print(students)

# len() ---- find an element at a position - list_name[index]
# .append() ------ add element to the END of the list: list_name.append(element)
# .insert() ------ add element at any index with list_name.insert(index, new_element)
# len() is a function and .insert() and .append() are methods
# numbers = [2, 4, 6]
# print(numbers[0])
# print(numbers)
# numbers.append(8)
# print(len(numbers))
# numbers.insert(1, 3)
# print(numbers)

# add multiple elements to a new list - both of these are added at the end
# new_numbers = numbers + [5, 6]
# print(new_numbers)
# access several values in a list using a colon between the indices - NOT inclusive of the last number
# list[index:index]
# print(new_numbers[0:3])
# print(numbers)
# print(numbers[0:2] + [5,6] + numbers[2:])

# .pop() removes an element 
# if there's no argument, it removes from the end, or you can pass the index as the argument. only takes an index as an argument
# you can return the value that was popped by putting it in a print statement. this is unique compared to other list methods - other ones won't return a value (like append)
# print(numbers.pop())
# print(numbers)
# numbers.pop(2)
# print(numbers)

# .remove() will search for an element and remove it. if there are multiple of the same elements, it just removes the first one
# numbers.insert(3, 4)
# numbers.remove(4)
# print(numbers)

# my_classmates = ["Jessica", "Melissa", "Diane", "Kevin"]
# print(len(my_classmates))
# print(my_classmates[2])
# first_classmate = my_classmates.pop(0)
# my_classmates.append(first_classmate)
# print(my_classmates)

# sum() adds the elements of a list, assuming there all ints / floats

# print the avg of the values in the list
# print(sum(more_numbers) / len(more_numbers))
# max() and min()) return the highest / lowest values in a list, whether it's a number or string
# other_numbers = [2, 4, 6]
# print(max(more_numbers))
# print(min(more_numbers))

# more_numbers = ["Melissa", "James", "Phillip", "William"]
# print(sum(other_numbers))

################LOOPS##################

# rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# print(rainbow)

# for loop - make up any name to represent the colors in the collection, then add the name of the collection
# for color in rainbow:
# 	print("~~~~")
# 	if len(color) > 3:
# 		print(color)
# 	print("----")	

# print(color)

# invitees = ["Nancy", "Jim", "Julia", "Clementine"]
# for guest in invitees:
# 	print(f"Why hello there, {guest}!")
# print("All of Team Nance has arrived.")

# for guest in invitees:
# 	guest = "Bob"
# print(invitees)
# ^ this won't actually update the list!

# # manual update
# invitees[0] = "Bob"
# print(invitees)

# for index, guest in enumerate(invitees):
# 	print(index, guest)
# 	if guest[-1] != "y":
# 		invitees[index] = guest + "y"

# print(invitees)

# strings are basically just a list of chars so you can access them using an index
# my_string = "Hello world"
# print(my_string[4])
# for char in my_string:
# 	print(char)

# for num in range(len(invitees)):
# 	print(num)
# 	print(f"{invitees[num]} gets a goody bag!")


name = list("Melissa")
print(name)
name = name + name[0] + "ay"
pig_latin_name = 
print(pig_latin_name)



# my_colors = ["purple", "pink", "blue", "green"]
# for color in my_colors:
# 	print(color)

# for index in range(len(my_colors)):
# 	color = my_colors[index]
# 	print(color)
# 	my_colors[index] = len(color)
# print(my_colors)

# to update values inside of a list, you need their index. otherwise you can't update it
# for index, color in enumerate(my_colors):
# 	print(color)
# 	my_colors[index] = len(color)

# print(my_colors)	

