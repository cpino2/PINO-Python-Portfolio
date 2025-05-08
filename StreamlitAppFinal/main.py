#IMPORTING LIBRARIES
import streamlit as st 
#importing streamlit library
import openpyxl
import spacy 
#importing spaCy library
import pandas as pd 
#import pandas library
from sklearn.ensemble import RandomForestClassifier 
#import meta estimator to train the model based on the uploaded dataset so it can make accurate predictions based on user input
from sklearn.model_selection import train_test_split 
#importing train_test_split function so the app can distinguish the training dataset (that which was imported to train the predictive model) from the test dataset (information inputted by the user when engaging with the app)
from spacy import displacy
#allows for entities to be visualized eventually in the app
from spacy.pipeline import EntityRuler
#importing spaCy's EntityRuler class from spaCy pipeline so user can add custom NER to spaCy pipeline when using this app
import re 
#necessary to extract punctuation and words from text user enters when engaging with the app
nlp = spacy.load("en_core_web_sm")#using this command to load the small English model from spaCy

#IMPORTING DATASET TO TRAIN MODEL
st.title("Predicting Risk of Developing Alzheimer's Disease Based on Demographic & Cognitive Features")#displaying app title on its screen
st.write("As the granddaughter of my wonderful, inspiring role model Abo who passed away from Alzheimer's disease at a young age, I am inspired to keep his legacy alive in all that I do. Hence, my project is created to honor him and the legacy he left behind. I hope to increase awareness about the risks of developing Alzheimer's disease so users can be proactive in taking the necessary precautions to mitigate their chances of the disease coming to fruition!")#providing user with a description about the app and its purpose to get them excited and intrigued
df = pd.read_csv("StreamlitAppFinal/alzheimersdataset.csv")#load sample dataset I created with alzheimer's data from my local device
st.write("Below is a sample of the Alzheimer's dataset I created based on research previously conducted at the National Institute of Health which I used to train the predictive model underlying this app! ")#write a caption above the preview of the dataframe that will be shown in my app
st.dataframe(df.head())#demonstrarte a sample of the dataframe I created on the actual app for the user to have a better understanding as to how the app predicts their risk of developing the disease/is able to see the cognitive and demographic factors the app takes into account when making this prediction
st.write("The number in the 'Education_Level' column is indicative of the number of years of schooling that individual has completed. In the 'Diagnosis' column, the 1 means the individual is at higher risk of developing the disease based on the data provided, whereas the 0 means the individual is at a lower risk of developing the disease.")#clarify significance of numerical values in the columns in the dataset shown
df = df[
    (df["APOE4_status"] != "Unsure") &
    (df["Family_history"] != "Unsure")
]#used boolean filtering to clean the dataset and remove the rows that had the response "unsure" about the apoe4 gene status since this "unsure" response just introduces ambiguity and will confuse the machine learning model
df["APOE4_status"] = df["APOE4_status"].map({"Yes": 1, "No": 0})#using label encoding to convert the string responses of "yes" and "no" in the "APOE4_status" column from strings to numeric values so the machine learning model can more easily predict the user's likelihood of developing the disease
df["Family_history"] = df["Family_history"].map({"Yes": 1, "No": 0})#using label encoding to convert the string responses of "yes" and "no" in the "Family_history" column from strings to numeric values so the machine learning model can more easily predict the user's likelihood of developing the disease
df["Sex"] = df["Sex"].map({"Male": 1, "Female": 0})#using label encoding to convert the string responses of "male" and "female" in the "Sex" column from strings to numeric values so the machine learning model can more easily predict the user's likelihood of developing the disease
#at this point, all of the dataset is made up of numeric values which will allow the machine learning model to properly predict the user's likelihood of developing Alzheimer's disease based on the data they provide when engaging with the app

#SHOWING TIDY DATASET
st.write("Below is a tidy version of the dataset used to train this model in which strings were converted to numeric values and 'unsure' responses were filtered out to ensure the predictive model runs smoothly.")#write a caption above the preview of the tidy dataframe that will be shown in my app
st.dataframe(df.head())#printing the tidy dataframe for the user to compare the differences between the tidy and untidy dataframe if they wish to do so, providing them the opportunity to understand the data that was used to train this model and make a prediction according to the responses the user provides
st.write(" In the 'APOE4_status' Column, the 1 means the individual carries the APOE4 gene, while the 0 means the individual does not carry the gene. Additionally, responses in this column that had previously been 'Unsure' were filtered out to maintain consistency within the predictive model! In the 'Family_history' column, the 1 means this individual has family history of Alzheimer's disease, while the 0 means they do not. Lastly, in the 'Sex' Column, the 1 means the individual is a male while the 0 means the individual is a female.")#clarify what changed between untidy and tidy dataset

#ASSIGNING INPUTS AND OUTPUTS
st.title("It's time for you to input data now!")#adding a caption so the user knows it is now time for them to input their own personal information while engaging with the app
X_features_inputs = df[["Age", "Sex", "Education_Level", "APOE4_status", "Family_history"]]#assigning the inputs that this model is going to use to make a prediction to "X" which represents the features
y_target_output = df["Diagnosis"]#assigning the output that the model is going to eventually predict to "y" which represents the target (the goal of the predictive model is to predict the likelihood of the user getting diagnosed with Alzheimer's disease based on the information they provide when engaging with the app)

#ABOUT RANDOM FOREST CLASSIFIER
model = RandomForestClassifier()#creating a new instance of random forest classifier (machine learning algorithm that will combine predictions made in trained model to make accurate predictions when interpreting user inputs from the app)
model.fit(X_features_inputs, y_target_output)#train the predictive model to consider the input features (sex, age, education level, APOE 4 status, family history) when predicting an output (high risk or low risk of developing Alzheimer's) so the model can learn patterns and be more accurate when making predictions based on user input
expander = st.expander("Click here to learn more about Random Forest Classifier:")
expander.write('''
    Random Forest Classifier is a meta estimator that is used to train the predictive model underlying this app. Learn more using the links below:\n
[Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)\n
[Distinguishing between data to train model and user input](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)\n
[More on scikit-learn](https://scipy-lectures.org/packages/scikit-learn/index.html)\n
[Algorithim Underlying Random Forest Classifier](https://www.e2enetworks.com/blog/random-forest-algorithm-in-machine-learning-a-guide)
''')

#USER ENGAGEMENT/INPUT
st.write("Type your age in the box below using numeric values!")#instructing user to type in their age
age_user_input = st.number_input("Age", min_value=0, max_value=120, value=0)#this provides the user the opportunity to input their age into a box provided with a minimum and maximum range value of 0-120 so that any user alive practically can use the app with a valid age input (even though the app is probably most likely going to be used by elderly people I just did not want it to be exclusive to a particular age group only!)
st.write("Click on the box below to select whether you are Male or Female.")#instructing user to select their sex
sex_user_input = st.selectbox("Sex", ["Male", "Female"])#this will display a select widget so the user can select their gender when inputting their personal data
st.write("Using the slider below, match the value to the appropriate number of years of education you have completed. 6 = completed through elementary school, 8 = completed through middle school/junior high, 12 = completed through high school, 14 = completed through college (associate's degree), 16 = completed through bachelor's degree, 18 = completed through master's/pHD")#adding caption to make the education completed portion easier on the user
education_user_input = st.slider("Years of Education Completed", min_value=0, max_value=18, step=1, value=0)#this displays a slider on the app for the user to adjust according to the years of school they have completed. the step =1 part ensures users can only respond to this portion of the app with whole number values
st.write("Click on the box below to select whether or not you carry the APOE4 Gene. \n Research has found that the presence of this gene influences the likelihood of Alzheimer's disease onset.")#caption to prompt the user to select whether or not they carry APOE4 gene
APOE4_user_input = st.selectbox("Do you carry the APOE4 Gene?", ["Yes", "No", "Unsure"])#this will display a selectbox for the user to input their response to the apoe4 gene question
st.write("Click on the box below to select whether or not you have family history of Alzheimer's disease.")#caption to prompt the user to select whether or not they have family history of Alzheimer's disease
family_history_user_input = st.selectbox("Do you have family history of Alzheimer's disease?", ["Yes", "No", "Unsure"])#this will display a selectbox for the user to input their response to the family history question

#ASSIGNING NUMERIC VALUES TO STRINGS
if APOE4_user_input == "Unsure" or family_history_user_input == "Unsure":#creating a condition if the user selects unsure as their response about the apoe4 gene or family history question
    st.warning("When using this app, it is required that you make your best guess and respond with either Yes or No to this question so the machine learning model can properly predict your likelihood of developing Alzheimer's disease based on your inputs.")#warning users to answer with either yes or no for the gene question and family history so the predictive model can function properly since unsure was already filtered out when tidying the dataset
else: #creating condition where users did not respond with unsure and data is ready to be used for the model to make a prediction based on the users inputs
    user_input_data = pd.DataFrame([{#converting user input into a dataframe that they will eventually be able to visualize after inputting all their information
        "Age": age_user_input,#calling the input the user typed in for age 
        "Sex": 1 if sex_user_input == "Male" else 0,#calling the input they selected for sex, yet, to keep values numeric/not have any strings so the model can accurately make predictions based on user input, the app is coded to display a 1 if the user inputted their sex as male and a 0 if they inputted their sex as female (using if else method to keep numeric values in dataset rather than strings)
        "Education_Level": education_user_input,#calling the input the user matched the slider to for education level 
        "APOE4_status": 1 if APOE4_user_input == "Yes" else 0,#calling the input they selected for APOE 4 status, yet, to keep values numeric/not have any strings so the model can accurately make predictions based on user input, the app is coded to display a 1 if the user inputted yes to the APOE status and a 0 if they inputted no (using if else method to keep numeric values in dataset rather than strings)
        "Family_history": 1 if family_history_user_input == "Yes" else 0#calling the input they selected for family history, yet, to keep values numeric/not have any strings so the model can accurately make predictions based on user input, the app is coded to display a 1 if the user inputted yes to having family history and a 0 if they inputted no (using if else method to keep numeric values in dataset rather than strings)
    }])

#VISUALIZING USER INPUT IN DATAFRAME
st.write("Below you can visualize your responses in a dataframe!")#creating caption so users know that dataframe appearing below reflects the information they just inputted when engaging with the app
st.dataframe(user_input_data)#displaying the dataframe with the information just inputted by the user 

#RISK PREDICTOR BUTTON
st.write("Click on the 'Risk Predictor' button below to see your results based on your inputs!")#encouraging user to click the button so the model can make a prediction based on their inputs and the way by which the model was previously trained, using the patterns it recognized/learned to make a prediction based on the user's input
if st.button("Risk Predictor"):#creates a button in app for the user to click 
    app_prediction = model.predict(user_input_data)[0]#calling the random forest model (meta estimator that was imported early on in the code to train the model based on the imported excel dataset) to specifically make a prediction about the data the app user inputted based on the way by which it was trained/the patterns it was trained to recognize
    st.subheader("Result of App Prediction Based on Input Provided:")#creating a header so the user knows that the prediction the app makes based on their input will appear below
    if app_prediction == 1:#creating a condition if the app were to predict the user were at high risk of developing Alzheimer's based on the input the user provided
        st.error("According to the provided inputs, you are at a higher risk of developing Alzheimer's disease.")#displays a red box to the user with a message to warn them they are at high risk...the red serves as a symbol of warning hence the st.error code used
    else:#creating a condition if the app were to predic tthe user were at lower risk of developing Alzheimer's disease
        st.success("According to the provided inputs, you are at a lesser risk of developing Alzheimer's disease.")#displays a green box to the user with a message to assure them they are at lower risk...the green is meant to serve as a symbol of safety and ensure the users that the information they received is good (given a "greenlight")

#CLOSING REMARKS/FURTHER USER EXPLORATION
st.title("Thank you for participating!")#thanking users for participating with the app
st.write("PSA: Please do NOT be alarmed at the prediction made by the model. The purpose of this app is solely to make you aware of your lifestyle/habits/genetic predispositions so that you can make the necessary adjustments early on to mitigate the chances of developing Alzheimer's disease!")#assuring users the app is not a definitive predictor as to whether or not they will develop the disease
st.title("Lifestyle Change Suggestions:")#creating title for a section in the app where users can browse to learn more about life style changes they can make to mitigate chances of disease coming to fruition by exploring the provided links below
st.write("According to previously conducted research, some lifestyle changes you can implement in your own life to reduce your chances of developing the disease (particularly if you carry the APOE4 gene, have family history of Alzheimer's disease, or have not completed many years of education) include adjusting your diet, minimizing alcohol consumption, and exercising regularly. Specifically, adopting a Mediterranean diet has been found to benefit those who carry the APOE4 gene in particular. A Mediterranean diet consists mainly of fresh fruits, vegetables, fish, nuts, and oils. Additionally, alcohol consumption is detrimental for brain health. In individuals who carry the APOE4 gene, alcohol seems to increase their risk of developing Alzheimer's disease, so it is wise for these people in particular to limit alcohol consumption. Exercise has also been found to lower a person's risk of developing Alzheimer's disease. Specifically, in people who carry the APOE4 gene, increased exercise has been found to be correlated with better cognitive functions and a decreased level of beta-amyloid plaques, which are highly indicative biomarkers of Alzheimer's disease.")#creating caption summarizing research about lifestyle changes that can be made to minimize risk of disease development 
st.write("If interested in learning more about the relation between Alzheimer's disease and genetic risk factors, you can explore: https://www.mayoclinic.org/diseases-conditions/alzheimers-disease/in-depth/alzheimers-genes/art-20046552")#providing link for users to learn more about tie to genetic risk factors if interested
st.write("If interested in learning more about lifestyle adaptations that can be made to mitigate the risk of the onset of Alzheimer's disease, you can explore: https://www.nia.nih.gov/health/alzheimers-and-dementia/preventing-alzheimers-disease-what-do-we-know")#providing link for users to learn more about general lifestyle changes they can make to minimize risk of developing the disease if interested 


