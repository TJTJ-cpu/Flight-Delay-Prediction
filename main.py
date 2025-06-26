from numpy import empty, empty_like
import pandas as pd
import matplotlib.pyplot as plt
import Utlis
import time

from sklearn.model_selection import train_test_split


df = pd.read_csv("data/airports.csv")
flightData = pd.read_csv("data/flights.csv")

airport = Utlis.GetRandomAirport()

print(flightData.columns)
print('airport')
print(df.columns)



