#would like to analyze the data in the carData.csv file
#this is a playground for that
#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('../data/train.csv')

def dataTransformationKmtoMiles(data):
    data["Miles_Driven"] = data["Kilometers_Driven"] * 0.621371
    return data

datatransformed = dataTransformationKmtoMiles(df)

# get the average kilometers driver by fuel type
df.groupby('Fuel_Type').mean()["Kilometers_Driven"].head().plot(kind='bar') 




# %%
