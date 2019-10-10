temperature = 90
ideal_temp = 75

while temperature >= ideal_temp:
	if temperature > ideal_temp:
		print(f"The temperature is {temperature} - crank the AC!")
	else:
		print(f"{temperature}. Ahh, that's better.")
	temperature -= 3
