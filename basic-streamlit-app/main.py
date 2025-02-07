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
color = st.color_picker("Pick the color that most resonates with your current mood:")

# Display the chosen color value
st.write(f"Take a second to think about how this color reflects your current state:)")

# ------------------------
# ADDING DATA TO STREAMLIT
# ------------------------

# Import pandas for handling tabular data
import streamlit as st
import pandas as pd

# Display a section title
st.subheader("Now that you've had a minute to ground yourself, let's begin looking at some fascinating penguin data!")

# Create a simple Pandas DataFrame with sample data
df = pd.DataFrame({
    'Island': ['Biscoe', 'Dream', 'Torgersen', 'Biscoe', 'Dream'],  # column listing the islands of these specific penguins in the order of id 20, 31, 130
    'ID': [20, 31, 131, 170, 305],
    'Species': ['Adelie', 'Adelie', 'Adelie', 'Gentoo', 'Chinstrap'],
    'Flipper Length (mm)': ['174', '178', '197', '209', '205'],  # Column of ID in respective order of each penguin listed
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male']  # Column of genders of each penguin listed
})

# Display a descriptive message
st.write("Here's a table categorizing some penguins in the dataset by their ID number, gender, and the respecive island they call home:")

# Display the dataframe in an interactive table.
# Users can scroll and sort the data within the table.
st.dataframe(df)

# ------------------------
# INTERACTIVE DATA FILTERING
# ------------------------

# Create a dropdown (selectbox) for filtering the DataFrame by city.
# The user selects a city from the unique values in the "City" column.
island = st.selectbox("Select an island", df["Island"].unique())

# Create a filtered DataFrame that only includes rows matching the selected city.
filtered_df = df[df["Island"] == island]

# Display the filtered results with an appropriate heading.
st.write(f"Penguins in {island}:")
st.dataframe(filtered_df)  # Show the filtered table

# ================================
# Step 3: Importing Data Using a Relative Path
# ================================

# Now, instead of creating a DataFrame manually, we load a CSV file
# This teaches students how to work with external data in Streamlit
df = pd.read_csv("data\penguins.csv")  # Ensure the "data" folder exists with the CSV file
# Display the imported dataset
st.write("Below is the (large) dataset loaded from a CSV file! Feel free to scroll through and admire its beauty!")
st.dataframe(df) #this lets you have access to the dataframe inside of your data folder

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