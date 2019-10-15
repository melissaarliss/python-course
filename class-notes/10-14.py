########### DICTIONARIES ##################

my_list = ["dog", "drink", "fruit"]

my_dict = {
	"puppy": "young dog",
	"tea": "herbal drink",
	"pineapple": "tropical fruit",
	"values": my_list,
	"my_bday": "December 5"
}

# dictionaries are unordered, unsorted - can't access by index
# values can be any data type. keys are basically always strings but are written in snake case

# look up values by their key, but can't find the key based on the value
# print(my_dict["puppy"])

# can validate if a key is in the dictionary, returns a bool
# print("dogs" in my_dict)

# add key-value pair to the dictionary
my_dict["mammoth"] = "wooly"

# reassingment / update a value in the dict
my_dict["pineapple"] = "prickly and sour"

# indicates the number of key value pairs in the dictionary
# print(len(my_dict))

# loop over a dictionary
# for key in my_dict:
# 	value = my_dict[key]
# 	if value[0] == "p":
# 		print(f"{key}: {my_dict[key]}")	
# 	elif len(key) == 3:
# 		print(f"{key}: {my_dict[key]}")


my_name = {
	"s": 1,
	"t": 1,
	"e": 2,
	"v": 1
}

# for key in my_name:
# 	if my_name[key] == 1:
# 		print(f"The letter {key} appears in my name {my_name[key]} once.")
# 	elif my_name[key] == 2:
# 		print(f"The letter {key} appears in my name {my_name[key]} twice.")


# name = "Melissa"
# letter_count = {}

# for letter in name:
# 	if letter in letter_count:
# 		letter_count[letter] += 1
# 	else:
# 		letter_count[letter] = 1

# print(letter_count)	

# for letter in letter_count:
# 	count = letter_count[letter]
# 	statement = f"My name has {count} {letter}"
# 	if count > 1:
# 		statement += "'s"
# 	print(statement)	
		
# words = ["pillow", "water", "hello", "pillow"]

# # creates a dictionary with the words in the list and how many times it appears
# def most_popular_word(collection):
# 	lookup = {}
# 	for item in collection:
# 		if item in lookup:
# 			lookup[item] += 1
# 		else:
# 			lookup[item] = 1	
# 	return lookup

# def find_most_popular(collection):
# 	# creates a dictionary using the most_popular_world function
# 	lookup = most_popular_word(words)

# 	# create a counter variable and variable for the word
# 	highest_number = 0
# 	popular_word = ""

# 	# loops through lookup dict and compares the current value to the counter, and resets the counter and the word if it's greater
# 	for word in lookup:
# 		if lookup[word] > highest_number:
# 			highest_number = lookup[word]
# 			popular_word = word	
	
# 	print(f"{highest_number}, {popular_word}")		

# find_most_popular(words)

state_capitals = {
  "Alaska" : "Juneau",
  "Colorado" : "Denver",
  "Oregon" : "Salem",
  "Texas" : "Austin"
  }

# def create_list(collection):
# 	# create a list from the values
# 	values = []
# 	for key in collection:
# 		values.append(collection[key])
# 	return(values)	

# capitals = create_list(state_capitals)

# print(capitals)

def reverse_lookup(dict, value):
	for state in dict:
		capital = dict[state]
		if capital == value:
			return state

print(reverse_lookup(state_capitals, "Denver"))






