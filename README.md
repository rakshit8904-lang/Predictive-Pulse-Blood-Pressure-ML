Predictive Pulse: Blood Pressure Analysis using Machine Learning

Predictive Pulse is a machine learning–based web application that predicts the risk of hypertension using patient health data. The system combines a trained ML model with a Django web interface to analyze medical information and provide risk assessment.

What the project does

Predicts hypertension (high blood pressure) risk

Classifies patients into different hypertension stages

Provides confidence score and clinical recommendations

Displays results through an interactive medical dashboard

Workflow

User enters patient information in the web interface.

Django backend collects and processes the input data.

The trained machine learning model analyzes the data.

The system predicts the hypertension risk level.

The result is displayed with risk classification and recommendations.

Technologies Used

Python

Django (web framework)

Scikit-learn (machine learning)

Pandas & NumPy (data processing)

HTML & CSS (frontend interface)

Joblib (model loading)

Input Features

Gender

Age

Medical history

Medication status

Symptoms (breath shortness, visual changes, nose bleeding)

Systolic and Diastolic blood pressure

Lifestyle factors such as diet

Output

Hypertension stage prediction

Confidence score

Clinical recommendations
