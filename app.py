import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
from list import all_features, all_disease
import datetime


app = Flask(__name__)

# Load the model from the pickle file
with open("logistic_regression_model.pkl", "rb") as file:
    model = pickle.load(file)


def classification(symptoms):
    symptoms = np.array(symptoms).reshape(1, -1)
    try:
        confidence = model.predict_proba(symptoms)
        top_three_indices = np.argsort(confidence[0])[::-1][:3]  # Get indices of top three confidences
        top_three_confidences = [
            {
                "confidence": confidence[0][idx],
                "prediction": all_disease[idx]

            } for idx in top_three_indices
        ]
        return top_three_confidences
    except AttributeError as e:
        print(f"Error: {e}")
        print(f"The loaded model does not have the 'predict' method.")


@app.route('/index', methods=['POST'])
def predict_disease():
    data = request.json
    input_array = [0] * 132
    symptoms = data['symptoms']
    for feature_name in symptoms:
        if feature_name in all_features:
            feature_index = all_features.index(feature_name)
            input_array[feature_index] = 1
    top_three_confidences = classification(input_array)  # Get top three confidences

    # Get the current time and date
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    response = {
        'diagnosis': top_three_confidences,
        'current_time': current_time,
        'current_date': current_date
    }  # Include top_three_confidences, current_time, and current_date in the response
    return jsonify(response)


@app.route('/')
def index():
    return render_template('symptoms.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
