employees = [
	{
	"name": "Ron Swanson",
 	"age": 55,
 	"department": "Management",
 	"phone": "555-1234",
 	"salary": "100,000"
	},
	{
	"name": "Leslie Knope",
 	"age": 45,
 	"department": "Middle Management",
 	"phone": "555-4321",
 	"salary": "90,000"
	},
	{
	"name": "Andy Dwyer",
 	"age": 30,
 	"department": "Shoe Shining",
 	"phone": "555-1122",
 	"salary": "50,000"
	},
	{
	"name": "April Ludgate",
 	"age": 25,
 	"department": "Administration",
 	"phone": "555-3345",
 	"salary": "60,000"
	}
]

for i in range(len(employees)):
	name = employees[i]["name"]
	department = employees[i]["department"]
	phone = employees[i]["phone"]
	print(f"{name} in {department} can be reached at {phone}.")



