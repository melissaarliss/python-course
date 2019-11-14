import requests
import geocoder
api_base_url = "https://api.darksky.net/forecast/71321cb803dc4539cd35795c6b9d3d78/"

destinations = ["Space Needle", "Crater Lake", "Golden Gate Bridge", "Yosemite National Park", "Las Vegas, Nevada", "Grand Canyon National Park", "Aspen, Colorado", "Mount Rushmore", "Yellowstone National Park",	"Sandpoint, Idaho", "Banff National Park", "Capilano Suspension Bridge"]

for place in destinations:
	lat = geocoder.arcgis(place).lat
	lng = geocoder.arcgis(place).lng
	full_api_url = (f"{api_base_url}{lat},{lng}")
	result = requests.get(full_api_url).json()
	summ = result["currently"]["summary"]
	temp = result["currently"]["temperature"]
	print(f"{place} is located at ({lat},{lng}). The weather is {summ} with a temperature of {temp}.")