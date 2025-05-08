# Project Overview
Purpose of App:
- Promote user exploration of spaCy's Named Entity Recognition Feature

Motivation Behind App:
-  Customize labels and patterns to visualize detected entities using spaCy's EntityRuler feature

Problem the App Solves: 
- Help users define and understand detected entities
  
## SpaCy's Approach to NER - Background 
<img width="1067" alt="image" src="https://github.com/user-attachments/assets/da44c4cd-e50f-423a-958e-f341dd7cd2e0" />
- Named Entity = Object that has a Proper Name (example: George Washington = Person)
- In Python, NER is the aspect of Natural Language Processing that focsues on classifying & identifying named entities
- Common Named Entities = Organizations, Person, Places, Date
- NER models understand Named Entities depending on the data they have been trained with!
- spaCy has a built in NER feature!
- After importing spaCy (as seen below), a sample text can be entered for spaCy's NER to analyze it with!

- <img width="227" alt="image" src="https://github.com/user-attachments/assets/a0b79337-556a-4d7c-845b-10a5280d1d1a" />

It is important to consider entity ruler must be added to the spaCy pipeline before NER if it does not already exist in spaCy pipeline, which can be done using the code below:
  
- <img width="316" alt="image" src="https://github.com/user-attachments/assets/fd48e21c-37fd-417a-a5c1-8417554f78c0" />
  
More detailed information can be found at any of these links: https://www.analyticsvidhya.com/blog/2021/06/nlp-application-named-entity-recognition-ner-in-python-with-spacy/ & https://spacy.io/api/entityrecognizer
## Set Up & Run
- To run the app locally, one must first ensure they are in the proper Python environment in Visual Studio Code (anaconda)
- Next, one must locate the proper folder in the terminal. This can be done as follows:
- <img width="599" alt="image" src="https://github.com/user-attachments/assets/c49d01c9-3112-4fa7-8293-35e128c93272" />
This should then take the user to an external browser from which they can engage with the app!
In the terminal, one must run "pip install spacy" and "python -m spacy download en_core_web_sm"
It is also necessary to import all requried libraries in the notebook for the streamlit app to function properly and the code to run error-free:
- Required libraries = streamlit, spaCy, pandas, 
- <img width="265" alt="image" src="https://github.com/user-attachments/assets/e91ccb2a-3945-4044-9923-fc714c4568fd" />
It is also necessary to load the small English model from spaCy for the NER app to work properly!
Upon installing the proper libraries, a requirements folder will appear in the NERStreamlitApp folder going through all of the libraries imported for the execution of the app's creation! This is what it will look like in that temporary folder created:
- <img width="752" alt="image" src="https://github.com/user-attachments/assets/691c1320-d308-45a9-a452-befabc04259b" />

- To deploy the app to Streamlit, one must log into their Streamlit Account on the Streamlit Community Cloud that should also be linked to their Github Account
- Next, one must click "Deploying? Free" on the top right corner of the screen
- Click "Create App" in the top right corner of the screen
- Click "Deploy a public app from Github"
- One must select the repository that stores their code, select the folder that stores their code, and select the name of their project specific repository as well as naming a URL that will become the link to the deployed version of the app!
  
# Link to deployed version of app on Streamlit Cloud:
- https://nerapppino.streamlit.app/
# App Features
- Upload text by typing in text box provided (sample text appears upon firt glance but user can type in box and override sample text with their own!)
- Define entity patterns based on preference of what words or punctuation user wants to analyze based on their custom input
- User can view output by following the instructions on the app and using the multiselect feature to insert words or punctuation that match with their desired label
Here is what the sample text looks like at first glance when users open the app:
- <img width="450" alt="image" src="https://github.com/user-attachments/assets/c0036914-b0eb-465e-aeff-57e8d7a111d3" />
If this were the text to have been analyzed, the output might look something like this, for example:
- <img width="434" alt="image" src="https://github.com/user-attachments/assets/20c0f9a5-e901-47d6-9538-50c40093e790" />
# References & Resources
- In the process of creating this app, I learned a lot about spaCy documentation!
- I became familiar with code lines such as "import re" which I learned was necessary to extract punctuation and words from text user enters when engaging with the app. You can learn more about this function here: https://spacy.io/usage/linguistic-features
- I also learned more about the EntityRuler itself, specifically its abilitiy to create custom patterns with corresponding labels, which the users are able to engage with through this app. More on this can be found here: https://ner.pythonhumanities.com/02_01_spaCy_Entity_Ruler.html
- I also became familiar with some organizational house-keeping tools to use for ease of engagement with the app for the user, such as the function "counter" which allowed the user to keep track of how many labels they added to analyze their text and the named entities that matched each!

# Visualizations of the App in Use
- Below is an image of named entities assigned to labels the user selected to analyze in the text they inputted!
<img width="557" alt="image" src="https://github.com/user-attachments/assets/70a1d9de-7ac5-4839-a684-a4edaac9754f" />

