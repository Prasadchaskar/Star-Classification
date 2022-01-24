import pickle
import numpy as np
import pandas as pd
import math
model = pickle.load(open('star.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
class_names = ['Galaxy','QSO','Star']

def predict(df):
    df = df[['alpha', 'delta', 'u','g', 'r', 'i','z','redshift']]
    df = scaler.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

						
