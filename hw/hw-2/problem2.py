angry = True
bored = False
hungry = True
tired = True

if angry and hungry and bored:
	print("Let's eat the Triceratops.")
elif tired and hungry:
	print("Let's eat the Iguanadon.")	
elif hungry and bored:
	print("Let's eat the Stegasaurus.")
elif tired:
	print("I'm going to bed.")
elif angry and bored:
	print("Let's fight the Velociraptor.")
elif angry or bored:
	print("Roar!")
else:
	print("Smile!")	








