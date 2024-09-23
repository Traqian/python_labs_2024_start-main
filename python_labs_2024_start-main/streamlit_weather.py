 # Convert the program to a Streamlit app. The temperature of all locations should be shown as bar chart.
import streamlit as st
import json
import pandas as pd
import altair as alt

# Read the JSON file
with open('weather.json', 'r') as f:
    weather_data = json.load(f)

# Create a DataFrame from the JSON data
data = {'Location': [], 'Temperature': []}
for location in weather_data['temperature']['data']:
    data['Location'].append(location['place'])
    data['Temperature'].append(location['value'])
df = pd.DataFrame(data)

# Create a bar chart
st.write("## Temperature of each location")
chart = alt.Chart(df).mark_bar().encode(
    x='Location',
    y='Temperature'
)
st.altair_chart(chart, use_container_width=True)

# Create a Streamlit app that allows the user to select a location from a dropdown menu
# and display the temperature of the selected location.
import streamlit as st
import json


# Read the JSON file
with open('weather.json', 'r') as f:
    weather_data = json.load(f)

# Create a list of locations
locations = [location['place'] for location in weather_data['temperature']['data']]
locations.insert(0, 'Select a location')

# Create a dropdown menu
selected_location = st.selectbox("Select a location", locations)

# Display the temperature of the selected location
if selected_location != 'Select a location':
    for location in weather_data['temperature']['data']:
        if location['place'] == selected_location:
            st.write(f"Location: {location['place']}")
            st.write(f"Temperature: {location['value']}")
            break
# Create a Streamlit app that allows the user to input a temperature value in Celsius
# and convert it to Fahrenheit.
import streamlit as st

# Create a text input box for the user to input the temperature in Celsius
celsius_temp = st.number_input("Enter the temperature in Celsius")

# Convert the temperature to Fahrenheit
fahrenheit_temp = (celsius_temp * 9/5) + 32

# Display the converted temperature
st.write(f"Temperature in Fahrenheit: {fahrenheit_temp}")
# Create a Streamlit app that allows the user to input a temperature value in Celsius
# and convert it to Fahrenheit.