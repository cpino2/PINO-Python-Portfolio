## Overview of my NER Streamlit App Project
- Purpose: Promote user exploration of spaCy's Named Entity Recognition Feature
- Features: Custom labels and patterns, visualization of detected entities using spaCy's EntityRuler feature
## SpaCy's Approach to NER - Background 
<img width="1067" alt="image" src="https://github.com/user-attachments/assets/da44c4cd-e50f-423a-958e-f341dd7cd2e0" />
- Named Entity = Object that has a Proper Name (example: George Washington = Person)
- In Python, NER is the aspect of Natural Language Processing that focsues on classifying & identifying named entities
- Common Named Entities = Organizations, Person, Places, Date
- NER models understand Named Entities depending on the data they have been trained with!
- spaCy has a built in NER feature!
- After importing spaCy (as seen below), a sample text can be entered for spaCy's NER to analyze it with!

- ##<img width="227" alt="image" src="https://github.com/user-attachments/assets/a0b79337-556a-4d7c-845b-10a5280d1d1a" />
  
- It is important to consider entity ruler must be added to the spaCy pipeline before NER if it does not already exist in spaCy pipeline, which can be done using the code below:
  
- ##<img width="316" alt="image" src="https://github.com/user-attachments/assets/fd48e21c-37fd-417a-a5c1-8417554f78c0" />
  
- More detailed information can be found at any of these links: https://www.analyticsvidhya.com/blog/2021/06/nlp-application-named-entity-recognition-ner-in-python-with-spacy/ & https://spacy.io/api/entityrecognizer
## Set Up Steps
# Running the App locally:
- Link to deployed version of app on Streamlit Cloud:
- Required libraries and installation commands: (snip it of code)
# App Features
- how user can upload text
- how user can define entity patterns
- how user can view output
- include example patterns and usage notes (screenshots)
# References
- link to spacy documentation (findall) and screenshot
- guides on using entityruler
- other resources i used
# visual examples
- screenshot showing app interface and output
