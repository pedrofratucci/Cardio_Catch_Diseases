import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, Response
from classes.cardio_catch_diseases import Cardio_Catch_Diseases
import json

# loading model trained from pickle file
with open('models/lgbm_model_tuned.pkl', 'rb') as file:
    model = pickle.load(file)

# initializing API
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def disease_predict():
    test_json = request.get_json()

    if test_json:

        # Unique Example
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])

        # multiple Example
        else:  # multiple Example
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # instantiating CDD class
        pipeline = Cardio_Catch_Diseases()

        # manipulating features
        test_raw_features = pipeline.features_engineering(test_raw)

        # rescaling features to predict
        test_raw_prepared = pipeline.data_preparation(test_raw_features)

        # predicting
        df_response = pipeline.get_predict(model, test_raw_prepared)

        return df_response

    else:

        return Response("{}", status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='10.0.0.33', port='5000')