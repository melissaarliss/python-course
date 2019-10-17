starting_word = input("Please enter a word: ")

def reverse_string(input):
	reversed_word = ""
	index = len(input)

	for letter in starting_word:
		reversed_word += starting_word[index - 1]
		index -= 1

	return(reversed_word)	

print(reverse_string(starting_word))

# print(starting_word[::-1])

# my_list = [1,2,3,4,5,6,7,8]
# start:end:step
# print(my_list[0:6:2])
# print every other element
# print(my_list[::2])
# print everything from the end
# print(my_list[::-1])

# for letter in starting_word:
# 	letter = letter + reversed_word

# print(reversed_word)