<html>
<head>
</head>
<body>
  <h1>Disease Diagnosis API</h1>
  <h2>Introduction</h2>
  <p>The Disease Diagnosis API is a Flask application that predicts the most probable diseases based on the provided symptoms. It uses a logistic regression model trained on a dataset of symptoms and corresponding diseases. The application provides an API endpoint to make predictions and returns the top three predicted diseases along with the current time and date.</p>
  <h2>Functionality</h2>
  <p>The main functionality of the Disease Diagnosis API is to classify a set of symptoms and provide the top three predicted diseases along with the current time and date. The API endpoint accepts a JSON payload containing a list of symptoms and returns a JSON response with the diagnosis results.</p>
  <h2>Setting Up and Running the Project</h2>
  <ol>
    <li>Clone the repository or download the project files.</li>
    <li>Ensure that you have Python 3 installed on your system.</li>
    <li>Install the required dependencies by running the following command in your terminal:
      <pre>pip install -r requirements.txt</pre>
    </li>
    <li>Place the trained model file (<code>logistic_regression_model.pkl</code>) in the project directory.</li>
    <li>Make sure the <code>list.py</code> file containing the feature and disease lists is also present in the project directory.</li>
  </ol>
  <h2>Using the Application</h2>
  <p>Once the project is set up and the dependencies are installed, you can run the Flask application using the following command:</p>
  <pre>python app.py</pre>
  <p>By default, the application will run on <a href="http://localhost:8080">http://localhost:8080</a>.</p>
  <h3>API Endpoints</h3>
  <p>The Disease Diagnosis API has the following endpoint:</p>
  <h4>POST /index</h4>
  <p>This endpoint accepts a JSON payload containing a list of symptoms and returns a JSON response with the diagnosis results. The payload should have the following structure:</p>
  <pre>
  {
    "symptoms": ["symptom1", "symptom2", "symptom3"]
  }
  </pre>
  <p>Replace <code>"symptom1"</code>, <code>"symptom2"</code>, <code>"symptom3"</code>, etc. with the actual symptoms you want to classify.</p>
  <p>The response will have the following structure:</p>
  <pre>
  {
    "diagnosis": [
      {
        "confidence": 0.85,
        "prediction": "disease1"
      },
      {
        "confidence": 0.78,
        "prediction": "disease2"
      },
      {
        "confidence": 0.62,
        "prediction": "disease3"
      }
    ],
    "current_time": "12:34:56",
    "current_date": "2023-07-04"
  }
  </pre>
  <p>The <code>"diagnosis"</code> field contains an array of objects, each representing a predicted disease. Each object has a <code>"confidence"</code> value indicating the confidence level of the prediction and a <code>"prediction"</code> value specifying the predicted disease.</p>
  <p>The <code>"current_time"</code> field provides the current time in the format "HH:MM:SS", and the <code>"current_date"</code> field provides the current date in the format "YYYY-MM-DD".</p>
  <h2>Additional Details</h2>
  <ul>
    <li>The trained model is loaded from the <code>logistic_regression_model.pkl</code> file using the <code>pickle</code> library.</li>
    <li>The <code>list.py</code> file contains the lists of all features (symptoms) and all diseases used by the application.</li>
    <li>The application assumes that the model file, the <code>list.py</code> file, and the <code>app.py</code> file are located in the same directory.</li>
    <li>The application utilizes the Flask web framework to handle HTTP requests and responses.</li>
    <li>The <code>index()</code> function renders a simple HTML template located in the <code>templates</code> directory, allowing users to input symptoms through a web interface.</li>
  </ul>
  <h2>Contributing and Issue Reporting</h2>
  <p>This project is currently not open for contributions. However, if you encounter any issues or have suggestions, please feel free to report them to the project maintainers.</p>
</body>
</html>
