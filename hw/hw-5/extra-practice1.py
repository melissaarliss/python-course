"""
1. Girl Scout Cookie Math
"""

# Print out the number of boxes of girl scout cookies that each girl in the troop sold in the below format:
	# Wendy: _____
	# Connie: _____
	# Francesca: _____

Wendy = {'tagalongs': 5, 'thin mints': 12, 'samoas': 8}
Connie = {'tagalongs': 10, 'thin mints': 4, 'samoas': 12}
Francesca = {'tagalongs': 18, 'thin mints': 14, 'samoas': 10}

salesW = Wendy["tagalongs"] + Wendy["thin mints"] + Wendy["samoas"]
salesC = Connie["tagalongs"] + Connie["thin mints"] + Connie["samoas"]
salesF = Francesca["tagalongs"] + Francesca["thin mints"] + Francesca["samoas"]

print(f"Wendy sold {salesW} boxes, Connie sold {salesC} boxes, and Francesca sold {salesF} boxes.")

# For each type of girl scout cookie, print out the total number of boxes sold in the below format:
        # tagalongs: _____
        # thin mints: _____
        # samoas: _____

total_tagalongs = Wendy["tagalongs"] + Connie["tagalongs"] + Francesca["tagalongs"]
total_thinmints = Wendy["thin mints"] + Connie["thin mints"] + Francesca["thin mints"]
total_samoas = Wendy["samoas"] + Connie["samoas"] + Francesca["samoas"]

print(f"{total_tagalongs} boxes of tagalongs were sold, {total_thinmints} boxes of thin mints were sold, and {total_samoas} boxes of samoas were sold.")

# For each type of girl scout cookie, print out the average number of boxes sold in the below format:
        # tagalongs: _____
        # thin mints: _____
        # samoas: _____

avg_tagalongs = total_tagalongs / 3
avg_thinmints = total_thinmints / 3
avg_samoas = total_samoas / 3

print(f"On average, each person sold {avg_tagalongs} boxes of tagalongs, {avg_thinmints} boxes of thin mints, and {avg_samoas} boxes of samoas.")

# Print out total the number of boxes of cookies the girls sold collectively as follows:
        # "This year we sold ______ boxes!"

boxes_sold = total_tagalongs + total_thinmints + total_samoas

print(f"This year we sold {boxes_sold} boxes in total.")



