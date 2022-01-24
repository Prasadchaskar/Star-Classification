import pickle
import numpy as np
import pandas as pd
import math
model = pickle.load(open('Steller/star.pkl', 'rb'))
scaler = pickle.load(open('Steller/scalar.pkl', 'rb'))
class_names = ['Galaxy','QSO','Star']

def predict(df):
    df = df[['alpha', 'delta', 'u','g', 'r', 'i','z','redshift']]
    df = scaler.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

						
alpha = 135.689107
delta = 	32.494632
u = 23.87882	
g = 22.27530	
r = 20.39501	
i = 19.16573	
z = 18.79371	
redshift = 0.634794
df = pd.DataFrame({ 
    'alpha':[alpha],
    'delta':[delta], 
    'u':[u], 
    'g':[g],
    'r':[r], 
    'i':[i],
    'z':[z],
    'redshift':[redshift]

})
print(predict(df))
