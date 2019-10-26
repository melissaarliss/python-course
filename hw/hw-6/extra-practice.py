class BankAccount():

	interest_rate = 1.02

	def __init__(self, balance=0):
		self.balance = balance
		print(f"Created an account.")

	def deposit(self, amt):
		if amt < 0:
			print("You can't deposit a negative amount.")
		else:
			self.balance += amt
			print(f"You deposited ${amt}. Your balance is now ${self.balance}.")	

	def withdraw(self, amt):
		if amt < 0:
			print("You can't withdraw a negative amount.")
		else:
			self.balance -= amt
			print(f"You withdrew ${amt}. Your balance is now ${self.balance}.")

	def accumulate_interest(self):
		self.balance *= BankAccount.interest_rate	
		print(f"You accumulated interest. Your balance is now ${self.balance}.")

class ChildrensAccount(BankAccount):

	interest_rate = 10

	def __init__(self, balance=0):
		super().__init__(balance)
		print("Created a children's account.")

	def accumulate_interest(self):
		self.balance += self.interest_rate
		print(f"You accumulated interest. Your balance is now ${self.balance}.")	

class OverdraftAccount(BankAccount):

	def __init__(self, balance=0, overdraft_penalty=40):
		super().__init__(balance)
		print("Created an overdraft account.")

	def withdraw(self, amt):
		if amt < 0:
			print("You can't withdraw a negative amount.")
		elif amt < self.balance:
			self.balance -= amt
			print(f"You withdrew ${amt}. Your balance is now ${self.balance}.")
		else:
			self.balance -= 40
			print(f"You don't have enough money in your account. Your balance is now ${self.balance}.")

	def accumulate_interest(self):
		if self.balance < 0:
			print(f"Your balance is ${self.balance}. You can't accumulate interest.")
		else:
			self.balance *= BankAccount.interest_rate	
			print(f"You accumulated interest. Your balance is now ${self.balance}.")		

basic_account = BankAccount()
basic_account.deposit(600)
basic_account.withdraw(17)
basic_account.accumulate_interest()

childs_account = ChildrensAccount()
childs_account.deposit(34)
childs_account.withdraw(17)
childs_account.accumulate_interest()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
overdraft_account.withdraw(12)
overdraft_account.accumulate_interest()





