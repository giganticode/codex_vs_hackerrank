"""
Task:\n You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on).
"""

import pandas as pd
import numpy as np

data = pd.read_csv('athlete_events.csv')

data.head()

data.shape

data.info()

data.describe()

data.isnull().sum()

data.dropna(inplace=True)

data.isnull().sum()

data.shape

data.head()

data.info()

data.describe()

data.columns

data.drop(['Name', 'Age', 'Height', 'Weight', 'Team', 'Games', 'Season', 'City', 'Sport', 'Event'], axis=1, inplace=True)

data.head()

data.info()

data.describe()

data.isnull().sum()

data.dropna(inplace=True)

data.isnull().sum()
