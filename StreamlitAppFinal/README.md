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
-  Ensure you are in the proper Python environment in Visual Studio Code (anaconda)
-  Import all requried libraries in the notebook for the streamlit app to function properly and the code to run error-free:
- Required libraries = streamlit, spaCy, pandas, scikit-learn, openpyxl
<img width="358" alt="image" src="https://github.com/user-attachments/assets/1d6a0af9-133a-4f22-b31a-cb1553b1c680" />


In terminal, 
- Must run "pip install openpyxl", "conda install openpyxl", "conda activate ner_app", "pip install openpyxl", "git add StreamlitAppFinal/alzheimersdataset.xlsx", "git commit -m "Add cleaned dataset", "git push origin main" so the excel file can be read and the predictive model can be trained properly
- Must run “pip install scikit-learn pandas openpyxl streamlit” to install required packages to use the model.predict() function later on to train the predictive model based on the loaded excel dataset
- I ended up saving my dataset as a ".csv" file eventually, yet I was initially striving to deploy the app using an excel file which is why all these commands were run in my terminal!
- Hence, it is not necessary to run these commands if using a ".csv" file, yet, I researched all about using an excel file before deciding to stick with a csv file so I am leaving all of the informaion here so the user can explore whichever way they wish.

 
Dependency list:
- Inside terminal, run "pipreqs" and a requirements.txt file will be created listing all necessary libraries
- Allows Streamlit to recreate necessary Python environment once deployed to Streamlit Community Cloud
- Must also add in spaCy language model because app works with spaCy (this is the URL in the image below that appears in the requirements.txt file)
- Here is how this dependency list should appear:
<img width="758" alt="image" src="https://github.com/user-attachments/assets/8b6ce7c3-0925-416e-9618-3ba9241a4c07" />


How to launch the app: 
- Next, locate the proper folder in the terminal:
<img width="571" alt="image" src="https://github.com/user-attachments/assets/823eab64-dc16-417e-ac43-637d79ad33a9" />

- Takes user to external browser to engage with app!

# App Features
User Inputs
- ID (way to distinguish patients from one another
- Age (numeric value in years)
- Sex (male = 1, female = 0)
- Education Level (years of school completed, key provided in app to aid user)
- APOE4 Status (yes = 1, no = 0, unsure = prompted to make an educated guess)
- Family History (yes = 1, no = 0, unsure = prompted to make an educated guess)

Main functions
- Predictive machine learning model was trained using an excel dataset created based on NIH data
- Model learns to recognize patterns amongst inputs and make a prediction based on those learned patterns
- App requires users to input data so model can predict high or low risk of Alzheimer's disease onset by recognizing patterns it learned as a result of being trained with the initial dataset

Outputs
- App predicts high or low risk of disease onsest based on user inputs
- 1 = High risk
- 0 = Low risk
- Strings converted to numeric values to ensure the predictive machine learning model functions error-free and runs smoothly

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
- Age Input - https://docs.streamlit.io/develop/api-reference/widgets/st.number_input
- Sex Input Select Box - https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox
- Education Level Input Slider Widget - https://docs.streamlit.io/develop/api-reference/widgets/st.slider
- Risk Predictor Button Output - https://docs.streamlit.io/develop/api-reference/status/st.warning

Training Predictive Model:
- Assigning Inputs & Outputs - https://discuss.streamlit.io/t/machine-learning/15457

Requirements File:
- About its function - https://medium.com/@mattplantz/using-streamlits-community-cloud-for-deployment-2c0659b1f07c

About Predictive Model:
- Random Forest Classifier: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- Distinguishing between data to train model and user input: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- More on scikit-learn: https://scipy-lectures.org/packages/scikit-learn/index.html
- Algorithim Underlying Random Forest Classifier: https://www.e2enetworks.com/blog/random-forest-algorithm-in-machine-learning-a-guide

Alzheimer's Disease Research:
- APOE4 Gene: https://www.mayoclinic.org/diseases-conditions/alzheimers-disease/in-depth/alzheimers-genes/art-20046552
- Lifestyle Changes to Mitigate Likelihood of Disease Onset: https://www.nia.nih.gov/health/alzheimers-and-dementia/preventing-alzheimers-disease-what-do-we-know

# Visualizations of the App in Use
The app demonstrates a visualization of the dataset that was used to train the predictive model so the user understands the patterns the model was trained to recognize, influencing the predictions it will make when taking into account inputs from the user.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/40764967-9c55-49c0-9df0-4eb3d5d68776" />


The app outputs a data table with the user's input values as well as a "low" or "high" risk warning based on the prediction made when taking into account the user's inputs and how they relate to the learned patterns the model recognizes as a result of having been trained with a dataset earlier on.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/8f888029-1244-4e2e-9700-e0dc4ad16648" />

The app also provides URL's that the user can browse if interested in learning more about risk factors and Alzheimer's disease. The sources come from the Mayo Clinic and the National Institute of Health, which are both renowned sources and highly trusted amoung the scientific community and in healthcare overall.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/39fa2af5-b2ef-4d1d-a6fc-975d692c8e13" />


