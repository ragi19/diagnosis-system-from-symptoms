# Diagnosis System from Symptoms

This project is a Flask application that uses a machine learning model to predict diseases based on symptoms.

## Setup

1. Clone the repository.
2. Install the dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```

## Dependencies

The project has the following dependencies:

- Flask
- numpy
- pickle
- pandas
- sklearn

## File Descriptions

- `app.py`: This is the main file of the application. It contains the Flask routes and the function for classifying symptoms.
- `list.py`: This file contains lists of symptoms and diseases, which are used in the classification process.