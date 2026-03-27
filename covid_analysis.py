import pandas as pd

data = pd.read_csv("covid_data.csv")

print("first 5")
print(data.head())

print("data informations")
print(data.info())

print("statistics data")
print(data.describe())