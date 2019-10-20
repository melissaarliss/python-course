users = {
	"person@email.com": "PassWord",
	"someone@email.com": "hiitsme",
	"me@email.com": "myPassword",
	"anyone@email.com": "IMawesome",
	"guy@email.com": "pa$$wordz"
}
current_user = {}

def set_current_user():
	username = input("Enter your username: ")
	current_user[username] = input("Enter your password: ")
	return(current_user)

def add_new_user():
	username = input("Enter a username: ")
	while username in users.keys():
		username = input("That username is already taken. Try again. ")
	users[username] = input("Enter a password: ")	
	return(users)

def check_password(dict, user):
	set_current_user()
	for user in current_user:
		current_password = current_user[user]
		if user in users.keys():
			if current_password in users.values():
				print("Login successful!")
				return
			else:
				print("Incorrect password. Try again.")	
				check_password(users, current_user)
		else:
			answer = input("That username does not exist. Would you like to create an account? ").lower().strip()
			if answer == "yes":
				add_new_user()
			else:
				return	

check_password(users, current_user)


