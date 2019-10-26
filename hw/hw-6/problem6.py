def kwargosaurus(**kwargs):
	for dino in kwargs:
		if kwargs[dino] == "smaller":
			print(f"{dino} is small! Mighty Kwargosaurus will fight you!")
		else:
			print(f"{dino} is big! Whimpering Kwargosaurus cries and runs away!")

print(kwargosaurus(Velociraptor="smaller", Stegosaurus="smaller", Triceratops="smaller", Trex="bigger"))