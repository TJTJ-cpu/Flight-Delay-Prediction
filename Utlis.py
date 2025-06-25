from numpy import empty
import pandas as pd
import matplotlib.pyplot as plt
import random



def GetAllAirportName():
    df = pd.read_csv("data/airports.csv")
    allAirport = df['name'].drop_duplicates()
    return allAirport

def GetRandomAirport():
    allAirportName = GetAllAirportName()
    name = random.choice(allAirportName)
    while (True):
        if bIsDataEmpty(name):
            name = random.choice(allAirportName) 
        else:
            return name


def GetAirportData(airportName):
    df = pd.read_csv("data/airports.csv")
    flightsData = pd.read_csv("data/flights.csv")
    aiportInfo= df[df["name"].str.contains(airportName)]
    airportId = aiportInfo["airport_id"].values[0] # Fake Error Here
    airportData = flightsData[(flightsData["OriginAirportID"] == airportId) | 
                        (flightsData["DestAirportID"] == airportId)]
    if not airportData.empty:
        print(f"Airport Name: {airportName}, ID: {airportId}")
    return airportData


def bIsDataEmpty(airportName):
    df = pd.read_csv("data/airports.csv")
    flightsData = pd.read_csv("data/flights.csv")
    aiportInfo= df[df["name"].str.contains(airportName)]
    airportId = aiportInfo["airport_id"].values[0] # Fake Error Here
    airportData = flightsData[(flightsData["OriginAirportID"] == airportId) | 
                        (flightsData["DestAirportID"] == airportId)]
    if airportData.empty:
        return True
    else:
        return False

