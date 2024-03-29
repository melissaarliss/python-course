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

translation = ""

def translate(beep, boop):
	total = beep + boop
	return alphabet[total-1]

for pair in message:
	if type(pair) == list:
		letter = translate(pair[0], pair[1])
		translation += letter
	else:
		translation += " "	

print(translation)





decoded_message = []

def decode():
	for pair in message:
		if type(pair) == list:	
			code = pair[0] + pair[1]
			letter = alphabet[code-1]
			decoded_message.append(letter)
		else:
			letter = " "
			decoded_message.append(letter)	
	real_translation = "".join(decoded_message)
	return(real_translation)

print(decode())


