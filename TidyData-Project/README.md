# Project Overview
Purpose of App:
- Apply the principles of tidy data to clean, transform, and do an exploratory data analysis on a dataset about olympic medalists.

Motivation Behind App: 
- Practice learning how to tidy datasets and transform them to make them easier to visualize/understand

Problem the App Solves:
- Facilitates data analysis and increases efficiency of interpreting results

## Set Up & Run
Directions
1. Import the dataset by either mounting google drive or calling upon the relative file path (dataset) once moved to the correct folder (in this case, that folder would by TidyData-Project). You can confirm that the dataset file is in the correct location by using the command "cd .\TidyData-Project" to locate the TidyData-Project folder. One can ensure they are in this folder by using the command "cd .\TidyData-Project\ ls" and this should result in the display of the appropriate folders that are within the TidyData-Project folder itself.
2. After the dataset is imported by having adjusted the file path being called upon depending on whether the user is running the code in google colab (can mount google drive) or visual studio code (needs to rely on relative file path), the user can run the notebook by clicking "Run All" on the top left of the notebook, as shown below
<img width="641" alt="image" src="https://github.com/user-attachments/assets/630eab9c-fb3b-4bdc-b677-067392ffb599" />

3. At this point, the user should begin to see their screen populate with data tables, pivot tables, and visualizations, along with markdown cells explaining all of the code and content it pertains to.
** It is important that the user understands the notebook will only run successfully if both pandas and seaborn are imported, as the code itself and visualizations rely on both the pandas library and the seaborn library.
   
Code Snippet I am Particularly Proud of:
- I learned how to drop the rows in the dataset with null values to make the dataframe more concise, which made it easier to create visualizations later in my project! Below is a snippet of the code I wrote to drop the null values in the Type of Medal column:
<img width="1064" alt="image" src="https://github.com/user-attachments/assets/9f83cf7c-ca1d-4fe4-9048-23966507a31d" />

To deploy the app to Streamlit,
- One must log into their Streamlit Account on the Streamlit Community Cloud that should also be linked to their Github Account
- Next, one must click "Deploying? Free" on the top right corner of the screen
- Click "Create App" in the top right corner of the screen
- Click "Deploy a public app from Github"
- One must select the repository that stores their code, select the folder that stores their code, and select the name of their project specific repository as well as naming a URL that will become the link to the deployed version of the app!

## App Features
1. Each variable forms a column.
2. Each observation forms a row.
3. Each value is a cell.
- Most tools in data analytics assume a tidy dataset, as it facilitates aggregating and analyzing data following this standard data structure of a tidy data foundation. Hence, tidy data principles allow for a standard way of organizing values in a dataset, facilitating data exploration and analysis (Wickham, 1).
About the Dataset
- The dataset was provided to me by Professor Smiley, my instructor, as he manipulated the original dataset so that there were missing values in the dataset so we could have the opportunity to practice what it means to transform an untidy dataset into a tidy dataset. This was done by melting the dataset, dropping null values, using str.split() functions to create distinct tables for each variable, and more. It is from the tidy dataset created that I was able to use tools such as pivot tables and data visualizations to come to conclusions and analyze trends we observe. Hence, there were many steps that went into this project, yet it was very fulfilling to watch my hardwork come to fruition.
  
## References & Resources: 
- I added hyperlinks to many sites throughout the project itself, yet these are some of the main sources I relied on to aid me in the process of compiling this project in the case anyone wants to read further into them.
- Pandas Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- Tidy Data Paper: https://vita.had.co.nz/papers/tidy-data.pdf
  
## Visualizations of the App in Use
- I had the opportunity to practice creating visualizations while putting together this project, some of which included barplots, histograms, and heatmaps (shown below, respectively).
<img width="428" alt="image" src="https://github.com/user-attachments/assets/4b04fd97-3425-417d-b13e-3d1e7a33d125" />
<img width="454" alt="image" src="https://github.com/user-attachments/assets/d4ce1f50-4576-4527-b669-6c68da77fbf2" />
<img width="443" alt="image" src="https://github.com/user-attachments/assets/38c4c280-9ddf-4c59-a08b-816c83d8aba2" />


