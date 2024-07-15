Spotify Song Like Predictor

This repository contains scripts for a machine learning project that predicts whether a user will like a song based on its attributes. The project includes data preprocessing, model training, evaluation, and deployment.
Table of Contents

    Project Overview
    Data Retrieval
    Data Preprocessing and Visualization
    Model Training and Evaluation
    Model Deployment
    Getting Started
    Contact

Project Overview

The Spotify Song Like Predictor project aims to predict the likelihood of a user liking a song based on various attributes such as danceability, energy, loudness, valence, etc. The project involves:

    Data retrieval from Spotify API.
    Data preprocessing and visualization.
    Training and evaluating a K-Nearest Neighbors (KNN) classifier.
    Deploying the model for user interaction.

Data Retrieval

The song attributes data was retrieved from the Spotify API. The process involves the following steps:

    Retrieve Access Token: Use a Python script to get an access token from the Spotify API. This token is used to authenticate and access the Spotify Web API.
    Fetch Song Data: Use another Python script that takes a Spotify song URL as input, fetches the song's attributes using the access token, and saves the data in a CSV file.

Scripts

    retrieve access token.py: This script retrieves an access token from the Spotify API.
    save song attributes to csv file.py: This script uses the access token to fetch song attributes for a given Spotify song URL and saves the data in a CSV file.

Data Preprocessing and Visualization

    Data Loading: Load the song attributes dataset from a CSV file.
    Visualization: Generate pair plots and distribution plots for various song attributes to understand the data.

Model Training and Evaluation

    Preprocessing: Handle missing data, scale numerical features, and split the data into training and test sets.
    Training: Train a K-Nearest Neighbors (KNN) classifier using GridSearchCV for hyperparameter tuning.
    Evaluation: Evaluate the model using accuracy, precision, recall, confusion matrix, and ROC curve.

Model Deployment

    User Input: Create a user-friendly interface for inputting song attributes.
    Prediction: Load the trained model and predict the likelihood of liking a song based on user input.
    Result Display: Display the prediction results.

Getting Started
Prerequisites

    Python 3.x
    Required libraries: pandas, sklearn, tensorflow, matplotlib, seaborn, joblib, requests

Installation

    Clone the repository:

    sh

git clone https://github.com/yourusername/spotify-song-like-predictor.git
cd spotify-song-like-predictor

Install the required libraries:

sh

    pip install -r requirements.txt

Running the Scripts

    Retrieve Access Token:

    sh

python retrieve_access_token.py

Fetch Song Data:

sh

python fetch_song_data.py

Model Training:

sh

python model_training.py

Model Deployment:

sh

    python model_deployment.py

Contact

For any questions or suggestions, feel free to contact me at uarif2093@gmail.com.
