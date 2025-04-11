import streamlit as st #importing streamlit library
import spacy#importing spaCy to ensure the installation was successful
from spacy import displacy
import re #this needs to be imported to separate sentences that do not have punctuation from those that do
nlp = spacy.load("en_core_web_sm")#using this command to make sure the small English model was downloaded
st.title("My NER Streamlit App")#displaying app title on its screen
import pandas as pd
#check this: to use the app, must run this in the terminal "streamlit run \Users\Owner\Documents\Test_Code\PINO-Python-Portfolio\NERStreamlitApp> streamlit run .\main.py"
st.write("I created this Streamlit app for users to explore spaCy's Named Entity Recognition with their own custom labels and patterns. The app usess spaCy's EntityRuler to add custom rules and visualize detected entities in the text the user chooses to upload!")
st.image("images/spacypipe.png")
# text = "Here is a sample text I am going to enter so you can then enter your own!"#entering a sample text so user knows what is meant by the app
text = st.text_area("Type anything in the text box below! This text will be analyzed by spaCy's Named Entity Recognition feature so you can see the detectd entities in the text you provide!")
st.write(text)
st.write("Below you will select labels and patterns for spaCy's NER to output custom entities that match those labels and patterns you want your text to be categorized by in this analysis!")
words = re.findall(r"[\w']+", text)
label = st.text_input("Type in the label for the pattern you wish to look at first in the box below:")
pattern_list = st.multiselect("In the text box below, enter the words that belong to the label you selected", options=words)
lp1 = []
for x in pattern_list:
    lp1.append([{"label":label, "pattern":x}])

continuous = st.selectbox("Let's add another label! Do you want to?", options=("", "yes", "No"))

#doc = nlp(text)#applying the NLP pipeline to the text to create a Doc container
# print(doc)#printing the text after having created a Doc container
# print(len(doc))#printing the length of the doc container
# print(len(text))#printing the length of the text without the doc container
# for token in text[:10]:
#     print (token)#printing off each character in text, including white spaces
# for token in doc[:10]:
#     print (token)#printing the tokens in the doc container to see the difference between text and doc even though they print the same sentence since the doc container has lots of attributes/metadata behind it
# tokens_spacy = [token.text for token in doc]#extracting tokens
# print(tokens_spacy)#printing the product of tokenization
# for sent in doc.sents:
#     print(sent)#using SBD (sentence boundary detection) to identify sentences in the provided
# sentence1 = list(doc.sents)[0]#grab first sentence only in the text provided, and must convert to list to iterate over the generator so as to not get an error
# print (sentence1)#print the first sentence of the provided text
# token2 = sentence1[2]#accessing one particular token "brown"
# print(token2)#printing the desired token we want to access to loop through the doc container using some token attributes
# token2.text#.text token attribute outputs the verbatim text content
# print(token2.text)
# token2.head#.head outputs the syntactic parent/governor of the token called, telling which word the token is governed by in the provided text
# print(token2.head)
# token2.lemma_#.lemma_outputs the base form of the token
# print(token2.lemma_)
# sentence1[4].lemma_#another test to show .lemma_ outputs the base form of the token called with no inflectional suffixes (it outputs do instead of doesn't when calling a token comprised of a contraction)
# print(sentence1[4].lemma_)
# sentence1[0].morph#.morph outputs the morphological analysis of the token called
# token2.pos_ #coarse-grained part of speech from the universal part of speech tag set for token 2 which was defined as the third word in sentence one ('brown')
# print(token2.pos_)
# print(sentence1[1].pos_)#printing part of speech for "quick"
# print(sentence1[6].pos_)#printing part of speech for "jumps"
# sentence2 = list(doc.sents)[1]#assigning sentence 2 to a variable and converting to list to iterate over the generator so there is no error found
# print(sentence2[3].pos_)#printing part of speech for "is"
# token2.tag_#list of fine-grained part of speech tags, which express the POS and some amount of morphological information, such as that a verb is past tense
# print(token2.tag_)
# for token in sentence1:
#   print (token.text, token.pos_, token.tag_)#iterating across each token(words and punctuations) in the first sentence of the text provided (hence the use of sentenec1) to identify its part of speech (POS tagging)
#   text_1 = """Barack Obama was the 44th President of the United States. He was born in Hawaii."""
# doc = nlp(text_1)#applying the NLP pipeline to the text to create a Doc container
# for ent in doc.ents:
#   print(ent.text, ent.label_) #recognizing lists of substsrings of the original text that have been identified as full named entities, such as a person, location, or organization, to conveniently extract all entities in the provided text
# for token in doc:
#   print(token.text, token.pos_)#outputs the entity label for specific tokens rather than substrings, as tokens are the smallest units of text (words or punctuations marks)
#   my_correct_sentence = "Chocolate chip cookie ice cream sandwiches are insanely delicious man I wish I could have one...every second."#uploading grammatically correct text
# doc_2 = nlp(my_correct_sentence) #applying the NLP pipeline to the text to create a Doc container
# for token in doc_2[:20]:#running the spacy pipeline on the grammatically correct text uploaded in the line of code above
#   print(token.text, token.pos_, token.tag_, token.lemma_)


# my_sentence = "Chocolate chip cokie; ice cream sangwich r insanely delishus man I wish I could have one... every second."#uploading grammatically incorrect statement
# doc_1 = nlp(my_sentence)#applying the NLP pipeline to the text to create a Doc container
# for token in doc_1[:20]:#running the spacy pipeline on the grammatically incorrect text uploaded in the line of code above to compare to the grammatically correct statement outputted prior to this one
#   print(token.text, token.pos_, token.tag_, token.lemma_)

# doc = nlp("SpaCy is an amazing NLP library.")
# for token in doc:
#     st.write(token.text, token.pos_)


#import streamlit as st #importing streamlit library
#st.markdown("Welcome to my NER Streamlit App") #displaying initial message
#st.title("NER Streamlit App")#displaying large title on the app screen
# st.image("flippers.png")#adding penguin image to app screen 
#st.write("I created this Streamlit app for users to explore spaCy's Named Entity Recognition with their own custom labels and patterns. The app usess spaCy's EntityRuler to add custom rules and visualize detected entities in the text the user chooses to upload!")
#st.write("Enter any text in the box below, and it will be analyzed using spaCy's Named Entity Recognition feature so you can visualize detected entities in your text of choice!")
#import streamlit as st#import streamlit
#import pandas as pd#import pandas
#import spacy#import spacy and displacy from spacy
#from spacy import displacy

# import spacy
# from spacy import displacy
# nlp = spacy.load("en_core_web_sm")
# text = st.text_area("Enter some text below:")
# if text:
#     doc = nlp(text)
#     st.subheader("Detected Entities:")
#     html = displacy.render(doc, style="ent")
#     st.components.v1.html(html, scrolling=True, height=300)


# import pandas
# import spacy
# from spacy import displacy
# import spacy #importing spaCy to ensure the installation was successful
# nlp = spacy.load("en_core_web_sm") #using this command to make sure the small English model was downloaded
# import spacy #importing spaCy
# nlp = spacy.load('en_core_web_sm') #loading spaCy's small English model and naming the object "nlp" so the script is easier to read



# if st.button("What is a penguin's favorite type of lettuce? Click here to find out!"):#creating a button for users to interact with and has a message that changes when the button is clicked by the users
#     st.write("Iceberg!🎉I hope I made you laugh!🚀")#this will appear when the button is clicked on by a user
# else:
#     st.write("Want to laugh? Click the button...")#if the button is not clicked, this phrase will appear until the button is clicked

# color = st.color_picker("Pick the color that most resonates with your current mood:")#this creates a color picker that is interactive for users so they can select a color

# st.write(f"Take a second to think about how this color reflects your current state:)")#this will be displayed under the chosen color to enforce users to consider the relationship between their selected color and their current state of being/mood
# st.slider('Slide this based on how you feel about the connection you established between the selected color and your current state. 1 = What connection? I am lost. 5 = Wow this color really speaks to me right now.', min_value=1, max_value=5)#introducing slider to promote further self-reflection for the user prior to engaging with the dataset
# import streamlit as st#adding data to streamlit
# import pandas as pd#importing pandas for handling data

# st.subheader("Now that you've had a minute to ground yourself, let's begin looking at some fascinating penguin data!") #this will be displayed as a title prior to the display of the data table

# df = pd.DataFrame({ #this is the code used to create pandas dataframe with some of the data from the large csv file
#     'Island': ['Biscoe', 'Dream', 'Torgersen', 'Biscoe', 'Dream'],  # column listing the islands of these specific penguins in the order of id 20, 31, 130
#     'ID': [20, 31, 131, 170, 305], #column listing penguins respective id numbers
#     'Species': ['Adelie', 'Adelie', 'Adelie', 'Gentoo', 'Chinstrap'], #column listing species of each penguin listed
#     'Flipper Length (mm)': ['174', '178', '197', '209', '205'],  # Column of ID in respective order of each penguin listed
#     'Gender': ['Female', 'Male', 'Male', 'Female', 'Male']  # Column of genders of each penguin listed
# # })

# # st.write("Here's a table categorizing some penguins in the dataset by the island on which they live, their ID number, their species, their flipper length in millimeters, and their gender:)") #this is a message that will appear describing the data shown in the datatable

# # st.dataframe(df) #this allows for the dataframe to be displayed in an interactive table from which users can scroll and sort the data how they wish

# # island = st.selectbox("Select an island", df["Island"].unique())#this creates a dropdown for users to filter the data by island, allowing the user to select an island from the identified 'island' column in the data table above

# # filtered_df = df[df["Island"] == island] #this creates a filtered dataframe based on the island the user selected and only inlcludes the data from the datatable that corresponds with the island selected by the user

# # st.write(f"Penguins in {island}:")#this message will appear to describe the penguins in the particular island selected by the user
# # st.dataframe(filtered_df)  # this will allow for the filtered table based on the island selection made by the user to be shown and viewable to the user

# # df = pd.read_csv("data\penguins.csv")  # this code imports the corresponding penguin data using a relative path so that a CSV file can be loaded by working with external data in Streamlit and it displays the imported dataset for users to view
# # st.write("Below is the (large) dataset loaded from a CSV file! Feel free to scroll through and admire its beauty!")#this message will appear on top of the dataset explaining to the users what they are viewing
# # st.dataframe(df) #this provides access to the dataframe inside the appropriate data folder

# # pip install spacy #install spaCy with a "!" since this is a Jupyter Notebook and we want to run a terminal command
# # python -m spacy download en_core_web_sm #installing the small English model of spaCy
# # import spacy #importing spaCy to ensure the installation was successful
# # nlp = spacy.load("en_core_web_sm") #using this command to make sure the small English model was downloaded
# import spacy #importing spaCy
# nlp = spacy.load('en_core_web_sm') #loading spaCy's small English model and naming the object "nlp" so the script is easier to read
# text = (
#     """The quick brown fox doesn't jump over the lazy dog. Natural Language Processing is fascinating!"""
#     )#importing the text for tokenization
# print(text)#printing text without having extracting yet tokens
# doc = nlp(text)#applying the NLP pipeline to the text to create a Doc container
# print(doc)#printing the text after having created a Doc container
# print(len(doc))#printing the length of the doc container
# print(len(text))#printing the length of the text without the doc container
# for token in text[:10]:
#     print (token)#printing off each character in text, including white spaces
# for token in doc[:10]:
#     print (token)#printing the tokens in the doc container to see the difference between text and doc even though they print the same sentence since the doc container has lots of attributes/metadata behind it
# tokens_spacy = [token.text for token in doc]#extracting tokens
# print(tokens_spacy)#printing the product of tokenization
# for sent in doc.sents:
#     print(sent)#using SBD (sentence boundary detection) to identify sentences in the provided
# sentence1 = list(doc.sents)[0]#grab first sentence only in the text provided, and must convert to list to iterate over the generator so as to not get an error
# print (sentence1)#print the first sentence of the provided text
# token2 = sentence1[2]#accessing one particular token "brown"
# print(token2)#printing the desired token we want to access to loop through the doc container using some token attributes
# token2.text#.text token attribute outputs the verbatim text content
# print(token2.text)
# token2.head#.head outputs the syntactic parent/governor of the token called, telling which word the token is governed by in the provided text
# print(token2.head)
# token2.lemma_#.lemma_outputs the base form of the token
# print(token2.lemma_)
# sentence1[4].lemma_#another test to show .lemma_ outputs the base form of the token called with no inflectional suffixes (it outputs do instead of doesn't when calling a token comprised of a contraction)
# print(sentence1[4].lemma_)
# sentence1[0].morph#.morph outputs the morphological analysis of the token called
# token2.pos_ #coarse-grained part of speech from the universal part of speech tag set for token 2 which was defined as the third word in sentence one ('brown')
# print(token2.pos_)
# print(sentence1[1].pos_)#printing part of speech for "quick"
# print(sentence1[6].pos_)#printing part of speech for "jumps"
# sentence2 = list(doc.sents)[1]#assigning sentence 2 to a variable and converting to list to iterate over the generator so there is no error found
# print(sentence2[3].pos_)#printing part of speech for "is"
# token2.tag_#list of fine-grained part of speech tags, which express the POS and some amount of morphological information, such as that a verb is past tense
# print(token2.tag_)
# for token in sentence1:
#   print (token.text, token.pos_, token.tag_)#iterating across each token(words and punctuations) in the first sentence of the text provided (hence the use of sentenec1) to identify its part of speech (POS tagging)
#   text_1 = """Barack Obama was the 44th President of the United States. He was born in Hawaii."""
# doc = nlp(text_1)#applying the NLP pipeline to the text to create a Doc container
# for ent in doc.ents:
#   print(ent.text, ent.label_) #recognizing lists of substsrings of the original text that have been identified as full named entities, such as a person, location, or organization, to conveniently extract all entities in the provided text
# for token in doc:
#   print(token.text, token.pos_)#outputs the entity label for specific tokens rather than substrings, as tokens are the smallest units of text (words or punctuations marks)
#   my_correct_sentence = "Chocolate chip cookie ice cream sandwiches are insanely delicious man I wish I could have one...every second."#uploading grammatically correct text
# doc_2 = nlp(my_correct_sentence) #applying the NLP pipeline to the text to create a Doc container
# for token in doc_2[:20]:#running the spacy pipeline on the grammatically correct text uploaded in the line of code above
#   print(token.text, token.pos_, token.tag_, token.lemma_)


# my_sentence = "Chocolate chip cokie; ice cream sangwich r insanely delishus man I wish I could have one... every second."#uploading grammatically incorrect statement
# doc_1 = nlp(my_sentence)#applying the NLP pipeline to the text to create a Doc container
# for token in doc_1[:20]:#running the spacy pipeline on the grammatically incorrect text uploaded in the line of code above to compare to the grammatically correct statement outputted prior to this one
#   print(token.text, token.pos_, token.tag_, token.lemma_)