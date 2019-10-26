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

cat = Animal()			
cat.say_hi()
cat.get_status()
cat.move()
cat.get_status()
cat.eat(30)	
cat.get_status()


