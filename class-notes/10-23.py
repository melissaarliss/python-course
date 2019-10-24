############## INHERITANCE ###########

# "superclass"
class Phone():
  def __init__(self, phone_number):
    self.number = phone_number

  def call(self, other_number):
    print("Calling from", self.number, "to", other_number)

  def text(self, other_number, msg):
    print("Sending text from", self.number, "to", other_number)
    print(msg)

# test_phone = Phone(5214)
# test_phone.call(515)
# test_phone.text(51121, "Hi!")

# IPhone is inheriting from Phone class. the parent class you're inheriting from is passed into the subclass when declaring it
class IPhone(Phone):
	def __init__(self, phone_number):
		# super calls the init method from the superclass - need this when constructing the subclass. pass in the same data as above
		super().__init__(phone_number)
		# don't need to set self.number here since that's set in the superclass
		# don't need this to be passed in in the init method - we set it in the setter method (set_fingerprint) later. it's not a default for all objects to have it, we can choose to set
		self.fingerprint = None
		self.unlocked = True

	# allows us to set a fingerprint later for a specific iphone object
	def set_fingerprint	(self, fingerprint):
		self.fingerprint = fingerprint
		self.unlocked = False

	def unlock(self, fingerprint):
		if fingerprint == self.fingerprint:
			print("Unlocked")
			self.unlocked = True
		else:
			print("Go away")
			self.unlocked = False	

	def text(self, other_number, msg):
		if self.unlocked:
			super().text(other_number, msg)
		else:
			print("You can't do that")				

# my_phone = IPhone(6906)	
# my_phone.set_fingerprint(999999)
# my_phone.text(5368, "Hi")	
