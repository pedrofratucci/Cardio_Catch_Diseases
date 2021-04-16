import pandas as pd
import numpy as np
import json
import pickle
import inflection


class Cardio_Catch_Diseases(object):

    def __init__(self):

        self.age_scaler = pickle.load(open('parameters/age_scaler.pkl', 'rb'))
        self.bmi_scaler = pickle.load(open('parameters/bmi_scaler.pkl', 'rb'))
        self.weight_scaler = pickle.load(open('parameters/weight_scaler.pkl', 'rb'))
        self.high_pressure_scaler = pickle.load(open('parameters/high_pressure_scaler.pkl', 'rb'))
        self.low_pressure_scaler = pickle.load(open('parameters/low_pressure_scaler.pkl', 'rb'))
        self.manual_selected_features = pickle.load(open('parameters/manual_selected_features.pkl', 'rb'))

    def features_engineering(self, df):

        '''creating and transforming datset's features'''

        # creating the dataset's new columns names
        new_columns = ['id', 'age', 'gender', 'height', 'weight', 'high_pressure', 'low_pressure', 'cholesterol',
                       'glucose', 'smoker', 'alcohol', 'active', 'cardio_disease']

        # changing the dataset's columns names for the 'new_columns' list values
        df.columns = new_columns

        # creating an array with the height column values in meters
        height_cm = df['height'].values / 100

        # creating a new dataframe column with the Body Mass Index value
        df['BMI'] = df['weight'].values / height_cm ** 2

        # modifying the 'age' column values for years, instead of days
        df['age'] = round(df['age'] / 365, ndigits=0).astype(int)

        return df

    def data_preparation(self, df):

        ''' preparing the dataset's features '''

        # rescaling numerical features
        df['age'] = self.age_scaler.transform(df[['age']].values)
        df['BMI'] = self.bmi_scaler.transform(df[['BMI']].values)
        df['weight'] = self.weight_scaler.transform(df[['weight']].values)
        df['high_pressure'] = self.high_pressure_scaler.transform(df[['high_pressure']].values)
        df['low_pressure'] = self.low_pressure_scaler.transform(df[['low_pressure']].values)

        return df

    def get_predict(self, model, df):

        ''' Filtering the features that will be used to predict and predict '''

        # selecting only the features that will be used to predict the result
        selected_features = self.manual_selected_features

        df_copy = df[selected_features].copy()

        # getting prediction
        df_copy['predict'] = model.predict(df_copy)

        # manipulating the return
        if df_copy['predict'][0] == 1:
            df_copy['answer'] = 'High probability of cardiovascular diseases'
        if df_copy['predict'][0] == 0:
            df_copy['answer'] = 'Low probability of cardiovascular diseases'

        return df_copy['answer'].to_json(orient='records')