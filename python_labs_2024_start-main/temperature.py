# Create a python script “temperature.py” to print the temperature of each location
# in the weather API response. The script should read the JSON file “weather.json”
# and print the temperature of each location in the following format:
#
# Location: Hong Kong
# Temperature: 27.3

import json

# Read the JSON file
with open('weather.json', 'r') as f:
    weather_data = json.load(f)

# Print the temperature of each location
for location in weather_data['temperature']['data']:
    print(f"Location: {location['place']}")
    print(f"Temperature: {location['value']}\n")

