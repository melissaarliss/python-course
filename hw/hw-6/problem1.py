contacts = {
	"Carly": "333-3333",
 	"Blondie": "444-4444",
 	"Jenny": "867-5309"
}

def get_contact(dict, name):
	if name in dict:
		print(f"The number of {name} is {dict[name]}.")
	else:
		print("Not found.")	

get_contact(contacts, "Carly")		
get_contact(contacts, "Will")