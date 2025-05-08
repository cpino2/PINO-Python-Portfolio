# Project Overview
Purpose of App:
- Increase awareness of lifestyle changes that can be made to mitigate likelihood of developing Alzhemier's disease
- Encourage user exploration to learn more about factors that influence their risk of developing Alzheimer's disease
- Make prediction based on user input as to whether or not the user is at high or low risk of developing the disease
  
Motivation Behind App:
- Inspired by my amazing Grandfather Abo who passed away from Alzheimer's disease a few years ago
- His battle with this struggle taught me lessons of perseverance, strength, and faith which I hope to share with others through this app
- My family and I have become more aware of our lifestyle habits ever since he was diagnosed
- I hope to encourage users to be proactive about their health so as to maximize their condition for as long as possible!
  
Problem the App Solves:
- Lack of Awareness - Detecting risk level (earlier rather than later) can encourage users to be proactive and make necessary lifestyle changes while making their health a priority before it is too late
  
![image](https://github.com/user-attachments/assets/f662b7ad-a937-4d08-a9b1-358ce5658568)

# Setup & Run
Local Installation Steps: 
-  Ensure in the proper Python environment in Visual Studio Code (anaconda)
-  Import all requried libraries in the notebook for the streamlit app to function properly and the code to run error-free:
- Required libraries = streamlit, spaCy, pandas, scikit-learn, openpyxl
<img width="309" alt="image" src="https://github.com/user-attachments/assets/2de95942-c557-4b95-bafe-6b271cf38d14" />
 
Dependency list:
- Create a requirements.txt file to install all necessary libraries all at once!
- Allows Streamlit to recreate necessary Python environment once deployed to Streamlit Community Cloud
- Here is how this dependency list should appear:
<img width="739" alt="image" src="https://github.com/user-attachments/assets/bd7133ec-8ea1-4abb-95d0-534bb095d8b5" />

How to launch the app: 
- Next, locate the proper folder in the terminal:
<img width="571" alt="image" src="https://github.com/user-attachments/assets/823eab64-dc16-417e-ac43-637d79ad33a9" />

- Takes user to external browser to engage with app!

# App Features
- Describe user inputs
- Main functions
- Outputs.

# References & Resources
Exploring Streamlit Community Cloud for Ideas about Disease Predictor Models:
- https://bihshtein-garmin-main-hufvkl.streamlit.app/
- https://github.com/arpy8/Alzheimers_Prediction_System/blob/main/Alzheimer's%20Prediction.ipynb

Dataset Used to Train Model
- Could not access dataset from National Institute of Health (NIH), so I created my own based on the following conclusions made from research conducted in the NIH
- https://www.nia.nih.gov/health/alzheimers-causes-and-risk-factors/alzheimers-disease-genetics-fact-sheet
- Here is what the Dataset I created looked like:

<img width="400" alt="image" src="https://github.com/user-attachments/assets/78b9855a-45d9-4aa8-9d95-6f79d30c4598" />


Streamlit Commands I learned more about while creating my app: 
- textbox: https://discuss.streamlit.io/t/how-to-add-a-streamlit-editable-code-editor-with-python-syntax-highlighting/54473/3

Stack Overflow:
- Label Encoding - https://stackoverflow.com/questions/24458645/label-encoding-across-multiple-columns-in-scikit-learn
- Filter out Responses to Tidy Dataset - https://stackoverflow.com/questions/37213556/remove-rows-that-contain-false-in-a-column-of-pandas-dataframe
- Excel File - https://stackoverflow.com/questions/74275058/importerror-missing-optional-dependency-openpyxl-use-pip-or-conda-to-install

Training Predictive Model:
- Assigning Inputs & Outputs - https://discuss.streamlit.io/t/machine-learning/15457

Requirements File:
- About its function - https://medium.com/@mattplantz/using-streamlits-community-cloud-for-deployment-2c0659b1f07c

# Visual Examples
- Embed screenshots showing the app in use.
