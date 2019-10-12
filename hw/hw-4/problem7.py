def cereal_time(breakfast):
	for cereal in breakfast:
		if cereal[-1] == "s":
			print(f"{cereal} are yummy!")
		else:
			print(f"{cereal} is yummy!")

cereal_time(["Froot Loops", "Cheerios", "Frosted Mini Wheats", "Capn Crunch"])				