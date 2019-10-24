############# OBJECTS AND CLASSES #################

# object = data + functionality
# everything is an object
# a list is a class - every list you make is an object, an instantiation of the list class - follows the same concept - you can append, pop, etc. (same thing with a dict, etc.)
# a class is a "template" for making instances that have similar qualities but all slightly different

class Dog():
	"""
	(This is a Docstring -  triple quotes for comments at the top of a class that can be accessed by other programmers / programs later and say what the class does)

	Dog class instantiates dog objects.

	Properties:
	- name
	- age
	- breed

	Methods:
	- bark
	- nap
	- age_in_human_years
	"""

	# class variable - associated with the class itself, not with the actual objects (so it doesn't come in the __init__ method)
	# often used to store info about the objects that are created from the class
	pack = []
	motto = "All dogs go to heaven."
	ct = 0

	# __init__ method indicates what data the class needs to be instantiated - very important in the class. the object will store and remember this information about itself
	# any class needs __init__ method in order to instantiate objects
	# can pass in default parameters in the __init__ method - objects will instantiate with this data
	# "instance variables"
	def __init__(self, name, age=0, breed="Mutt"):
		self.name = name
		self.age = age
		self.breed = breed
		Dog.pack.append(self.name)
		Dog.ct += 1
		print(f"A dog is born. Now there are {Dogs.ct} dogs.")

	# creating an instance method
	# whenever you create an instance method (including __init__) you need self as the first arg
	def bark(self):
		print(f"Woof, my name is {self.name}.")	

	def nap(self):
		if self.age < 5:
			print("zzzz")
		else:
			print("zZzZzZzZzZzZzZzZ")	

	def age_in_human_years(self):
		h_years = self.age * 7			
		print(f"My age in human years is {h_years}.")

# can access a class attribute even before any objects are instantiated
# print(Dog.pack)

# instantiating
# daisy is an object (a variable), an instantation of Dog class
# in the background it's calling Dog.__init__() but you don't need to write that
# daisy = Dog("Daisy", 2, "Cocker Spaniel")	
# blu = Dog("Blu", 4, "Golden Doodle")
# sam = Dog("Sam", 10, "Lab")
# t_swift = Dog("Taylor Swift")

# print(Dog.motto)
# print(Dog.pack)
# print(Dog.ct)

# can also access a class variable like this (with the name of the related object) but convention is to use the class name
# refers to the class's knowledge - even though daisy was created before the other dogs, it still knows about other objects instantiated after it
# print(daisy.pack)

# prints data from the variable
# print(daisy.name)
# print(t_swift.breed)

# calls instance method and injects its own data
# daisy.bark()
# daisy.nap()
# sam.nap()
# t_swift.bark()
# sam.age_in_human_years()

class TeaCup():
	def __init__(self, capacity, amount):
		self.capacity = capacity
		self.amount = amount
		print(f"This teacup is holding {self.calc_perc()}% of its capacity.")

	# the print statement in __init__ can still access this data even though calc_perc is called below it	
	def calc_perc(self):
		return round((self.amount / self.capacity), 2) * 100

	def fill(self, amt):	
		self.amount += amt
		if self.amount > self.capacity:
			print("Help, I'm overflowing!")
		print(f"Now this teacup has {self.amount} oz. It's at {self.calc_perc()}% capacity.")

	def drink(self, amt):
		if self.amount == 0:
			print("There's nothing in this cup. You can't drink it!")
		elif amt > self.amount:
			print(f"You only drank {self.amount} oz. The cup is now empty.")
			self.amount = 0
		else:
			self.amount -= amt
			print(f"You drank {amt} oz. Now this teacup has {self.amount} oz in it.")		

# cup = TeaCup(8, 8)
# cup.drink(1)

class Band():
	ct = 0
	valid_genres = ("pop", "rock", "r&b")

	def __init__(self, genre, band_name, albums_released=0):
		# "input validation" - only creates objects if it's in the valid_genres tuple
		if genre not in Band.valid_genres:
			print("I don't know that genre.")
		else:	
			self.genre = genre
			self.band_name = band_name
			self.albums_released = albums_released
			Band.ct += 1
			print(f"There are now {Band.ct} bands created.")

	def print_stats(self):
		print(f"The {self.genre} band {self.band_name} has {self.albums_released} albums released.")	

# queen = Band("rock", "Queen", 15)		
# ts = Band("pop", "Taylor Swift", 5)

# this will overwrite the previous queen object
# queen = Band("pop", "The Beatles", 10)

# won't allow this obj to be instantiated since it's a different genre
# other = Band("deadmau5", "electronica", 8)
# print(Band.number_of_bands)




class Bank():
	total_balance = 0

	def __init__(self, account_type, balance=0):
		self.account_type = account_type
		self.balance = balance
		Bank.total_balance += self.balance
		print(f"Created an account. The total balance is now ${Bank.total_balance}.")

	def deposit(self, amt):
		self.balance += amt
		Bank.total_balance += amt
		print(f"Your balance is now ${self.balance}.")	

	def withdraw(self, amt):
		self.balance -= amt
		Bank.total_balance -= amt
		print(f"Your balance is now ${self.balance}.")	

bank = Bank("savings", 100)



