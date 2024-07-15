## README

### Project Overview

This project focuses on building and deploying a machine learning model to predict the likelihood of a user liking a song based on its attributes. The process involves data retrieval from Spotify, model training, and deployment. The key components of this project include:

1. Data Retrieval
2. Model Training
3. Model Deployment

### Data Retrieval

The song attributes data was retrieved from the Spotify API. The data retrieval process consists of two main scripts:

1. **Retrieve Access Token**: This script, `retrieve_access_token.py`, is used to get an access token from the Spotify API. The access token is necessary for authenticating and accessing the Spotify Web API.
   
2. **Fetch Song Data**: This script, `fetch_song_data.py`, takes a Spotify song URL as input, fetches the song's attributes using the access token, and saves the data in a CSV file. This ensures we have a structured dataset of song attributes that can be used for model training.

### Model Training

The model training script performs several key tasks to prepare and train a machine learning model:

1. **Data Preprocessing**: The script reads the song attributes data, checks for missing values, and scales the numerical features to ensure consistency.

2. **Data Visualization**: Various plots are generated to visualize the distributions of song attributes and their relationship with the target variable, providing insights into the data.

3. **Feature Selection**: The features (attributes) and the target variable are separated for model training.

4. **Model Training and Evaluation**: Multiple classifiers, including K-Nearest Neighbors (KNN), are evaluated. Hyperparameter tuning is performed using GridSearchCV to find the best parameters for the KNN model. The performance of the model is evaluated using accuracy, precision, recall, confusion matrix, and ROC curve.

5. **Model Saving**: The trained KNN model is saved to a file for later use in the deployment phase.

### Model Deployment

The model deployment script utilizes the trained KNN model to predict the likelihood of a user liking a song based on its attributes. The process involves:

1. **Loading the Trained Model**: The saved KNN model is loaded from the file.

2. **User Input**: The script prompts the user to input values for various song attributes.

3. **Prediction**: The input values are processed and fed into the model to predict the probability of liking the song.

4. **Result Display**: The likelihood of liking the song is displayed to the user, providing a clear and actionable output based on the model's prediction.

### Conclusion

This project demonstrates a comprehensive workflow for building and deploying a machine learning model using data retrieved from the Spotify API. By including the scripts for data retrieval, model training, and deployment, the project ensures transparency and reproducibility, making it a valuable resource for anyone interested in music data analysis and machine learning applications.
