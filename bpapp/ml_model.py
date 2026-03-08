import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR,'hypertension_model.pkl'))

def predict_bp(data):

    data = np.array(data).reshape(1,-1)

    prediction = model.predict(data)

    return prediction[0]