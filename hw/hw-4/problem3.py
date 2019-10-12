starting_word = input("Enter a word or sentence. ")
reversed_word = ""
index = len(starting_word)

for letter in starting_word:
	reversed_word += starting_word[index - 1]
	index -= 1

print(f"Backwards, that's {reversed_word}.")