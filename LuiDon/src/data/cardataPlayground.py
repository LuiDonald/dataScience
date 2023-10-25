#would like to analyze the data in the carData.csv file
#this is a playground for that
#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os
import sys
import datetime
import time
import re
import logging


# %%
df = pd.read_csv('../data/train.csv')

def dataTransformationKmtoMiles(data):
    data["Miles_Driven"] = data["Kilometers_Driven"] * 0.621371
    return data

datatranformed = dataTransformationKmtoMiles(df)


# %%
