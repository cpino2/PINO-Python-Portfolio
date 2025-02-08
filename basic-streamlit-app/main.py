import streamlit as st #importing streamlit library

st.markdown("Hi there, friend!") #displaying initial message

st.title("Flippers in the Air like They Just Don't Care!")#displaying large title on the app screen
st.image("flippers.png")#adding penguin image to app screen 

st.write("This is an app I created to foster self-awareness by way of exploration and adventure! It invites users to evalute their feelings and mental state prior to engaging with an interactive data analysis about penguins. Users can direct their analysis of this dataset based on their interests and preferences in terms of selections, highlighting the uniqueness of the personal interactions embedded into this app!") #displaying initial message

if st.button("What is a penguin's favorite type of lettuce? Click here to find out!"):#creating a button for users to interact with and has a message that changes when the button is clicked by the users
    st.write("Iceberg!🎉I hope I made you laugh!🚀")#this will appear when the button is clicked on by a user
else:
    st.write("Want to laugh? Click the button...")#if the button is not clicked, this phrase will appear until the button is clicked

color = st.color_picker("Pick the color that most resonates with your current mood:")#this creates a color picker that is interactive for users so they can select a color

st.write(f"Take a second to think about how this color reflects your current state:)")#this will be displayed under the chosen color to enforce users to consider the relationship between their selected color and their current state of being/mood
st.slider('Slide this based on how you feel about the connection you've established between your color and your current feeling', 1 = I am so confused, what connection? & 5 = Wow, this color really speaks to me right now!', min_value=1, max_value=5)
import streamlit as st#adding data to streamlit
import pandas as pd#importing pandas for handling data

st.subheader("Now that you've had a minute to ground yourself, let's begin looking at some fascinating penguin data!") #this will be displayed as a title prior to the display of the data table

df = pd.DataFrame({ #this is the code used to create pandas dataframe with some of the data from the large csv file
    'Island': ['Biscoe', 'Dream', 'Torgersen', 'Biscoe', 'Dream'],  # column listing the islands of these specific penguins in the order of id 20, 31, 130
    'ID': [20, 31, 131, 170, 305], #column listing penguins respective id numbers
    'Species': ['Adelie', 'Adelie', 'Adelie', 'Gentoo', 'Chinstrap'], #column listing species of each penguin listed
    'Flipper Length (mm)': ['174', '178', '197', '209', '205'],  # Column of ID in respective order of each penguin listed
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male']  # Column of genders of each penguin listed
})

st.write("Here's a table categorizing some penguins in the dataset by the island on which they live, their ID number, their species, their flipper length in millimeters, and their gender:)") #this is a message that will appear describing the data shown in the datatable

st.dataframe(df) #this allows for the dataframe to be displayed in an interactive table from which users can scroll and sort the data how they wish

island = st.selectbox("Select an island", df["Island"].unique())#this creates a dropdown for users to filter the data by island, allowing the user to select an island from the identified 'island' column in the data table above

filtered_df = df[df["Island"] == island] #this creates a filtered dataframe based on the island the user selected and only inlcludes the data from the datatable that corresponds with the island selected by the user

st.write(f"Penguins in {island}:")#this message will appear to describe the penguins in the particular island selected by the user
st.dataframe(filtered_df)  # this will allow for the filtered table based on the island selection made by the user to be shown and viewable to the user

df = pd.read_csv("data\penguins.csv")  # this code imports the corresponding penguin data using a relative path so that a CSV file can be loaded by working with external data in Streamlit and it displays the imported dataset for users to view
st.write("Below is the (large) dataset loaded from a CSV file! Feel free to scroll through and admire its beauty!")#this message will appear on top of the dataset explaining to the users what they are viewing
st.dataframe(df) #this provides access to the dataframe inside the appropriate data folder


# Play around with more Streamlit widgets or elements by checking the documentation:
# https://docs.streamlit.io/develop/api-reference
# Use the cheat sheet for quick reference:
# https://cheat-sheet.streamlit.app/

### Challenge:
# 1️⃣ Modify the dataframe (add new columns or different data).
# 2️⃣ Add an input box for users to type names and filter results.
# 3️⃣ Make a simple chart using st.bar_chart().