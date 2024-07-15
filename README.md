# README

## Spotify Song Like Prediction Model

This project consists of two main scripts: one for training a machine learning model to predict whether a user will like a song based on its attributes, and another for deploying this model to make predictions based on user input.

### Project Structure

- **Training Script (`spotify model training.py`)**: This script handles the data preprocessing, feature scaling, model training, evaluation, and saving the trained model.
- **Deployment Script (`spotify model deployment.py`)**: This script loads the trained model, takes user input for song attributes, and predicts the likelihood that the user will like the song.

### Training Script

1. **Libraries Used**:
    - Pandas for data manipulation and analysis
    - Scikit-learn for data preprocessing, model training, and evaluation
    - TensorFlow for neural network modeling
    - Seaborn and Matplotlib for data visualization
    - Joblib for saving and loading trained models

2. **Data Preprocessing**:
    - Load the dataset from a CSV file.
    - Visualize the dataset to understand the distribution of various attributes.
    - Handle missing values and scale numerical features using StandardScaler.
    - Split the dataset into training and testing sets.

3. **Model Training**:
    - Train a K-Nearest Neighbors (KNN) classifier using GridSearchCV for hyperparameter tuning.
    - Evaluate the model using metrics such as accuracy, precision, recall, and confusion matrix.
    - Visualize the model's performance using confusion matrix and ROC curve.

4. **Model Saving**:
    - Save the trained KNN model to a file using Joblib for later use in the deployment script.

### Deployment Script

1. **Libraries Used**:
    - Pandas for creating a DataFrame from user input
    - Joblib for loading the trained model

2. **User Input**:
    - Prompt the user to input values for various song attributes such as acousticness, danceability, energy, etc.

3. **Prediction**:
    - Load the trained KNN model from the file.
    - Use the model to predict the likelihood of the user liking the song based on the input attributes.
    - Output the predicted likelihood to the user.

### How to Run the Scripts

1. **Training Script**:
    - Ensure you have the necessary libraries installed.
    - Place the dataset file (`song_attributes.csv`) in the specified path.
    - Run the script to preprocess the data, train the model, and save the trained model to a file.

2. **Deployment Script**:
    - Ensure the trained model file is in the specified path.
    - Run the script and follow the prompts to input song attributes.
    - The script will output the likelihood of liking the song based on the input attributes.

### Notes

- The project uses a K-Nearest Neighbors classifier, but other models such as Logistic Regression, Decision Tree, Gaussian Naive Bayes, Support Vector Classifier, and Random Forest are also available for experimentation.
- Ensure the paths to the dataset and model files are correctly specified in the scripts.
- The training script includes visualizations to help understand the data and model performance.
- The deployment script provides a simple user interface to input song attributes and get predictions.

### Future Enhancements

- Incorporate additional models and compare their performance.
- Implement a more sophisticated user interface for the deployment script.
- Explore feature engineering techniques to improve model accuracy.
