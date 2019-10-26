class Animal():
	def __init__(self, energy=50):
		self.energy = energy
		print("I am coming to life!")

	def eat(self, amount):
		self.energy += amount

	def move(self):
		self.energy -= 10
		print("I am running!")		

	def get_status(self):
		print(f"My current energy level is {self.energy}.")
		if self.energy < 0:
			print("I'm starving!")
		elif self.energy < 50:
			print("I'm getting hungry...")	
		elif self.energy < 100:
			print("I'm happily full.")	
		else:
			print("I'm stuffed!")		

	def say_hi(self):
		print("Meep!")

class Penguin(Animal):
	def __init__(self, energy=100):
		super().__init__(energy)
		print("I am a penguin!")	

	def move(self):
		self.energy -= 5
		print("I am sliding!")

penguin = Penguin()
penguin.get_status()
penguin.move()
penguin.get_status()
penguin.eat(20)
penguin.get_status()

class Eagle(Animal):
	def __init__(self, energy=20):
		super().__init__(energy)
		print("I'm an eagle!")

	def move(self):
		if self.energy < 0:
			print("I'm too tired to fly.")
		else:
			self.energy -= 20
			print("I'm flying to the sea!")

	def say_hi(self):
		print("Shrieek!")	

eagle = Eagle()
eagle.get_status()
eagle.move()
eagle.get_status()
eagle.move()
eagle.move()
eagle.eat(40)
eagle.get_status()
eagle.say_hi()



