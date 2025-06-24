import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split


df = pd.read_csv("data/airports.csv")
flightData = pd.read_csv("data/flights.csv")


lax_info = df[df["name"].str.contains("Los Angeles")]
laxId = lax_info["airport_id"].values[0] # Fake Error Here

laxFlight = flightData[(flightData["OriginAirportID"] == laxId) | 
                        (flightData["DestAirportID"] == laxId)]
delayTime = 15

laxFlight.loc[:, "IsDelayed"] = laxFlight["DepDelay"] > delayTime

features = laxFlight[["DayofMonth", "DayOfWeek", "Carrier"]]
labels = laxFlight["IsDelayed"]

# Convert Category into one-hot encoded variables (dummy)
features_encoded = pd.get_dummies(features, columns=["Carrier"])

# Get the list of columns
carrier_columns = [col for col in features_encoded.columns if col.startswith("Carrier_")]

# Create a graph of number of flight per carrier
dfCarrierData = features_encoded[carrier_columns].sum()

#Sort by value
dfSortedCarrierData = dfCarrierData.sort_values()

if True:
    dfSortedCarrierData.plot(kind='barh', figsize=(10,6))
    plt.title("Number of Flights per Carrier (LAX)")
    plt.xlabel("Flights")
    plt.show()






