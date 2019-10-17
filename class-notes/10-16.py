####### DEFAULT ARGS #############

# default args - setting it equal in the function definition
def add_multiple(x,y=0,z=1):
	return x+y+z

# if you add a default arg in the original function, you don't need to rewrite
# print(add_multiple(1))	

# or you can add them and overwrite them
# print(add_multiple(1,2,3))


############ ONE ASTERISK ARGS #################

# with one asterisk - *args - allow you to pass in any number of args and sees it as a list
# def add_vars(*args):
# 	sum = 0

# need to use a for loop since you don't know how many args there will be
# 	for num in args:
# 		sum += num

# 	return sum

# print(add_vars(4,5,6))		


########## TWO ASTERISK ARGS ##############

# with two asterisks - ** - is a stand in for a dictionary
kwargs = {
	"strawberries" : 3,
	"mangos" : 4,
	"mochi" : 10
	}

def froyo_shop(**kwargs):
	for topping in kwargs:
		num = kwargs[topping]
		print(num, topping)

# treats these like dictionary entries
# froyo_shop(strawberries=3, mangos=4, mochi=10, blueberries=9)

# adding ** in the call will treat the dictionary in the same way
# froyo_shop(**kwargs)

# this won't work - it is looking for dictionary-like entries
# froyo_shop(kwargs)


############### SETS #################

# sets are like lists but can't hold duplicate values

# this is a list - it has dupes
listserv = [
	"bob@me.com",
	"bob@me.com",
	"joe@pub.com",
	"sal@web.com"
]

youtube_subscribers = [
	"joe@pub.com",
	"sal@web.com",
	"hello@hello.com",
	"hello@hello.com"
]

# cast a list into a set to remove dupes
unique_listserv = set(listserv)
unique_youtube = set (youtube_subscribers)

# find the unique values by getting the len of a set
# print(len(unique_listserv))

# can't index a set
# print(unique_listserv[0])

# but you can loop over it and grab the elements
# for item in unique_listserv:
# 	print(item)

# cast a set back into a list - this will remove the duplicate values and the new list will be de-duped
# unique_listserv = list(unique_listserv)

# use .difference() to find the differences between two sets
# print(unique_listserv.difference(unique_youtube))

# or subtract them to find what is not in each set, but be careful of the order
# print(unique_listserv - unique_youtube)
# print(unique_youtube - unique_listserv)

# add an element to a list - it doesn't go at the end, just somewhere in the set
unique_listserv.add("hi@hi.com")
# print(unique_listserv)

# can't add something that's already in the list
unique_listserv.add("bob@me.com")
# print(unique_listserv)

# remove something from a list
unique_listserv.remove("hi@hi.com")
# print(unique_listserv)


############# TUPLES #############

# IMMUTABLE data structure - data can't be changed. can't add or remove items. like a list but uses parentheses
rainbow = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")

# can be indexed
# print(rainbow[0])

# and looped over
# for color in rainbow:
# 	print(color)

# these don't work
# rainbow.pop()
# rainbow.append("red")

# convert a list into a tuple by casting it, or the other way around
my_list = ["hi", "hello", "hey"]
my_list = tuple(my_list)
# print(type(my_list))

# rainbow = list(rainbow)
# print(type(rainbow))


########### DICTIONARIES ############

shopping_cart = {
	"rugs": 300,
	"lamps": 100,
	"couches": 500
}

# get the total of all the objects
# counter = 0
# for item in shopping_cart:
# 	quantity = shopping_cart[item]
# 	counter += quantity
# print(counter)

# get a list of the keys or the values in the dictionary. not ~technically~ a list but kinda like it
# print(shopping_cart.keys())
# print(shopping_cart.values())

# can get the sum since it behaves like a list
# print(sum(shopping_cart.values()))

# use .items() method to iterate over keys and values in a dictionary
counter = 0
for item, quantity in shopping_cart.items():
	counter += quantity
	print(item, quantity)

print(counter)








