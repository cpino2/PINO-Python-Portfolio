# Import the Streamlit library
import streamlit as st

# Display a simple text message
st.write("Hi there, friend!")

# Display a large title on the app
st.title("Flippers in the Air like They Just Don't Care!")

# ------------------------
# INTERACTIVE BUTTON
# ------------------------

# Create a button that users can click.
# If the button is clicked, the message changes.
if st.button("What is a penguin's favorite type of lettuce? Click here to find out!"):
    st.write("Iceberg!🎉I hope I made you laugh!🚀")
else:
    st.write("Want to laugh? Click the button...")

# ------------------------
# COLOR PICKER WIDGET
# ------------------------

# Creates an interactive color picker where users can choose a color.
# The selected color is stored in the variable 'color'.
color = st.color_picker("Pick a color")

# Display the chosen color value
st.write(f"You picked: {color}")

# ------------------------
# ADDING DATA TO STREAMLIT
# ------------------------

# Import pandas for handling tabular data
import streamlit as st
import pandas as pd

# Display a section title
st.subheader("Now let's take a look at some penguin data!")

# Create a simple Pandas DataFrame with sample data
df = pd.DataFrame({
    'Island': ['Biscoe', 'Dream', 'Torgersen'],  # column listing the islands of these specific penguins in the order of id 20, 31, 130
    'ID': [20, 31, 131],  # Column of ID in respective order of each penguin listed
    'Gender': ['Female', 'Male', 'Male']  # Column of genders of each penguin listed
})

# Display a descriptive message
st.write("Here's a simple table:")

# Display the dataframe in an interactive table.
# Users can scroll and sort the data within the table.
st.dataframe(df)

# ------------------------
# INTERACTIVE DATA FILTERING
# ------------------------

# Create a dropdown (selectbox) for filtering the DataFrame by city.
# The user selects a city from the unique values in the "City" column.
city = st.selectbox("Select a city", df["City"].unique())

# Create a filtered DataFrame that only includes rows matching the selected city.
filtered_df = df[df["City"] == city]

# Display the filtered results with an appropriate heading.
st.write(f"People in {city}:")
st.dataframe(filtered_df)  # Show the filtered table

# ------------------------
# NEXT STEPS & CHALLENGE
# ------------------------

# Play around with more Streamlit widgets or elements by checking the documentation:
# https://docs.streamlit.io/develop/api-reference
# Use the cheat sheet for quick reference:
# https://cheat-sheet.streamlit.app/

### Challenge:
# 1️⃣ Modify the dataframe (add new columns or different data).
# 2️⃣ Add an input box for users to type names and filter results.
# 3️⃣ Make a simple chart using st.bar_chart().