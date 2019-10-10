"""
2 beeps, 6 boops
0 beeps, 5 boops
9 beeps, 3 boops
4 beeps, 8 boops
10 beeps, 5 boops
BOP! (pretty sure this is a space!)
11 beeps, 12 boops
5 beeps, 5 boops
1 beep, 17 boops
5 beeps, 7 boops
4 beeps, 0 boops
"""

# create a list of lists for the beeps and boops
# grab the two ints in the inner list 
# add the ints together to get a value
# grab the letter at that index in the alphabet string
# print the letter

import string
alphabet = string.ascii_uppercase

message = [
	[2, 6],
	[0, 5],
	[9, 3],
	[4, 8],
	[10, 5],
	"BOP",
	[11, 12],
	[5, 10],
	[1, 17],
	[5, 7],
	[4, 0]
]

translated_letters = ""

def translate(beep, boop):
	total = beep + boop
	return(alphabet[code-1])

for pair in message:
	if type(pair) == list:
		translate(beep, boop)


			code = beep + boop
			letter = alphabet[code-1]
			# print(letter)
			translated_letters.append(letter)
		else:
			letter = " "	
	# print(translation)
	real_translation = "".join(translated_letters)
	print(real_translation)	

print()





