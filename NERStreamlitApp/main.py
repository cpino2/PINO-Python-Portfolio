import streamlit as st #importing streamlit library
import spacy#importing spaCy library
import pandas as pd #import pandas library
from spacy import displacy#allows for entities to be visualized eventually in the app
from spacy.pipeline import EntityRuler#importing spaCy's EntityRuler class from spaCy pipeline so user can add custom NER to spaCy pipeline when using this app
import re #necessary to extract punctuation and words from text user enters when engaging with the app
nlp = spacy.load("en_core_web_sm")#using this command to load the small English model from spaCy
st.title("My NER Streamlit App Project!")#displaying app title on its screen
st.write("I created this Streamlit app for users to explore spaCy's Named Entity Recognition with their own custom labels and patterns. It usess spaCy's EntityRuler to add custom rules and visualize detected entities in the text the user chooses to upload! Let's have some fun with this!")#providing user with a description about the app and its purpose to get them excited and intrigued
text = st.text_area(
     "Type anything in the text box below! This text will be analyzed by spaCy's Named Entity Recognition feature so you can see the detected entities in the text you provide!",
     placeholder="My name is Ceci and I am having fun learning to code!"
     )#instructing user to input text so it can be analyzed by spaCy's NER feature and used placeholder to input a sample text so as to provide more guidance to the user/make instructions more clear
st.write("You entered:")#printing this so reader can have confirmation their text was entered properly
st.write(text)#printing text entered by user so they know their desired text was entered properly (confirmation)
st.write("Below you will select labels and patterns for spaCy's NER to output custom entities that match those labels and patterns you want your text to be categorized by in this analysis!")#printing instructions on app so user can define custom entities on the app by selecting the patterns/labels by which they want spaCy's NER feature to analyze their desired text entered above 
words_and_punc = re.findall(r"[\w']+|[.,!?;()]", text)#extracting all words and punctution from the text entered by the user to then put them into a multiselect so users can more easily define their custom entities/engage with the app
label = st.text_input("Type in the label for the pattern you wish to look at in the box below:")#creating a text input box for user to type in label they want to look at first (part of defining custom entities)
pattern_list = st.multiselect("In the text box below, enter the words or punctuation that belong to the label you selected", options=words_and_punc)#creates a multiselect dropdown with options to enter being any of the words or punctuation in the text the user entered above (part of defining custom entities in the app)
user_list = [{"label": label, "pattern": word_and_punc} for word_and_punc in pattern_list]#this creates a list of key-value pairs (a dictionary) that pairs the words or punctuation the user selected with the label they chose
list_sublists = [user_list]#creates a list to hold entity patterns and specifically the list is initialized with the first key-value pair defined above by the user
adding_another_label = st.selectbox("Do you want to add another label?", options=["", "Yes", "No"])#gives user the option to add another label if they want to 
counter = 1#this lets the user keep track of how many labels they have defined during their engagement with the app, promoting ease of use and helping users understand the results they see when engaging with the app
while adding_another_label == "Yes":#creation of this loop lets users add more labels so long as they respond "Yes" when prompted to add another label if they want to
    st.write(f"Define Label {counter + 1}:")#shows user the label number they are defining to help the user keep track of how many labels they have already defined
    label1 = st.text_input(f"Enter label name for label {counter + 1}:", key=f"label{counter}")#prompting user to select a new label to analyze and enter its name
    pattern_list1 = st.multiselect(f"Select words for label {counter + 1}:", options=words_and_punc, key=f"pattern{counter}")#creates a multiselect dropdown with options to enter being any of the words or punctuation in the text the user entered above (part of defining custom entities in the app)
    new_user_list = [{"label": label1, "pattern": word} for word in pattern_list1]#creates another list to hold entity patterns
    list_sublists.append(new_user_list)#adds list that was just created to the list of sublists created above that was initialized with the first key-value pair the user defined above using the append function
    counter += 1#this allows the user to keep track of how many labels they have added while engaging with the app
    adding_another_label = st.selectbox(f"Do you want to add label {counter + 1}?", options=["", "Yes", "No"], key=f"continue{counter}")#asks user if they want to add another label again
if "entity_ruler" not in nlp.pipe_names:#if entity ruler does not already exist in spaCy pipeline, this function adds entity ruler to the pipeline before NER
    ruler = nlp.add_pipe("entity_ruler", before="ner")
else:#in the case that entity ruler already exists in the spaCy pipeline,
    ruler = nlp.get_pipe("entity_ruler")#this function just calls forth the entity ruler that already exists in the pipeline
for sublist in list_sublists:#this function calls forth all the key value pairs that were appended to the list_sublists above
    ruler.add_patterns(sublist)#it adds all the key value pairs that were appended to the list_sublists to the entity ruler itself so that spaCy's NER feature can analyze the custom entities defined by the user
doc = nlp(text)#creating a doc so text entered by user can be processed by spaCy's NER feature (this includes analyzing and extracting custom defined entities)
show = displacy.render(doc, style="ent", jupyter=False)#here is where we see why it was necessary to import displacy from spaCy so that the user can actually visualize the entities specific to the text they entered when using the app
st.markdown(show, unsafe_allow_html=True)#this results in the actual display of the detected entities 