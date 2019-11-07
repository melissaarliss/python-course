############## WORKING WITH APIS ####################

# import requests library
import requests

# get request. URL must be a string
# an API "endpoint" is just a URL where the data sits
# response = requests.get("http://api.open-notify.org/astros.json")
# format into json / python dictionary. without parsing into json, it will just return an http response
# response = response.json()
# print(response)
# sometimes helpful to print the keys in a dict so that you know what you're working with so that you know how it's structured
# print(response.keys())
# print(response["people"][1]["name"])

# output = []
# for people_dict in response["people"]:
# 	output.append(people_dict["name"])
# print(output)

# HTTP codes:
# 200 codes = good
# 300 codes = need to reroute but still okay
# 400 codes = can't find it
# 500 codes = server error

weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Lavonia,us&appid=052f26926ae9784c2d677ca7bc5dec98")
weather_data = weather_data.json()
print(weather_data)




