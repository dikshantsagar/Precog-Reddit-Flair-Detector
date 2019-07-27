# Precog-Reddit-Flair-Detector
Reddit Flair Detector
Heroku App URL - https://redditflairdetector.herokuapp.com

 # Work Flow
 
 - Fetching Data
 - Processing Data
 - Trying Analysing Different Models
 - Training the Final Model
 - Creating a WebApp(Django)
 - Integrating WebApp and Trained Model
 - Deploying the Integration
 
 
 ## Fetching Data
 
 Module Used - PRAW https://praw.readthedocs.io/en/latest/ [using the Reddit API]\
 Attributes used from the Submission object from the module to train the model
 - title
 - text
 - comments
 - flair (only for training target)
 
 <b>Reddit only allowed 1000 submissions to be fetched at any point of time\
 due to which only 944 usable datapoints were available to train the model</b>
 
 ## Processing Data
 
 The attributes(all text) were combined into one single string cleaned\
 Then a DataFrame was created in the form  [text] - [flair]
 
 ### Tokenizers Tried
 - CountVectorizer
 - CountVectorizer + TFIDF transformer
 - TFIDF
 
 better results were achieved with TFIDF alone so in the final model\
 it was used.
 
 ## Trying Analysing Different Models and Creating the Final Model
 
 Models Tried
 - Logistic Regression
 - Naive Bayes
 - SVM
 - Neural Network
 
 Better results were achieved by SVM overall as shown in the analysis plot.
 ![alt text](https://raw.githubusercontent.com/dikshantsagar/Precog-Reddit-Flair-Detector/master/readmeimages/15.png?token=AHRBHFVGX5UPSSYGPOVWVLK5IUO7I)
 
 So final model trained was an SVM. To utilise them in the App two pickle dumps were created one for the TFIDF vectorizer\
 and one for the SVM model.
 
 Model Accuracy Achieved with such less data ~ <b>0.66</b>
 
 
 ## F1 Score for SVM on Train and Test
 
 <b> 0.657 </b>
 
 ## Creating the WebApp and Integrating 
 
 Clearly Django was the way to go as it works in python it became easy to integrate the ML model\
 into the App
  ![alt text](https://raw.githubusercontent.com/dikshantsagar/Precog-Reddit-Flair-Detector/master/readmeimages/11.png?token=AHRBHFQR6TCWM4W4OOQI4JC5IUOXU)
   ![alt text](https://raw.githubusercontent.com/dikshantsagar/Precog-Reddit-Flair-Detector/master/readmeimages/12.png?token=AHRBHFWLWNBXR3KHSIJLB3C5IUO24)
    ![alt text](https://raw.githubusercontent.com/dikshantsagar/Precog-Reddit-Flair-Detector/master/readmeimages/13.png?token=AHRBHFWL6DWHIBG36UM3RUK5IUO4A)
     ![alt text](https://raw.githubusercontent.com/dikshantsagar/Precog-Reddit-Flair-Detector/master/readmeimages/14.png?token=AHRBHFUU3V6WVCJTSUWJD3K5IUO5Y)
 
 ## Final Deploying 
  
  The WebApp was deployed on Heroku with a python buildpack a great easy to use platform.
  
 
 # Directory Structure
 - MongoDB Collection ( contains mongodb collection export file )
 - reddit[f] (the WebApp Folder)
 - notebooks[f] (Jupyter notebooks containing scripts)
 - static[f] (static files for the App)
 - templates[f] (django html templates for the App)
 - requirements.txt (a list of requirements required for heroku deploy)
 - other App related files (model objects,procfile,.csv format data,.gitignore ,etc)
 
 # Modules and frameworks Used
 - Praw
 - Scikit-Learn
 - Django
 - Pandas
 - Keras
 - Nltk
 - matplotlib
 - Pickle
 - Chartjs
