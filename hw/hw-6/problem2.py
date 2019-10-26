def letter_counter(word):
	counts = {}
	for letter in word:
		if letter not in counts:
			counts[letter] = 1
		else:
			counts[letter] += 1	
	return counts

print(letter_counter("Melissa"))
print(letter_counter("hi there"))		