from numpy import empty
import pandas as pd
import matplotlib.pyplot as plt
import random
import os

from pandas.io.common import file_path_to_url



def GetAllAirportName():
    df = pd.read_csv("data/airports.csv")
    airportArr = df['name'].drop_duplicates().tolist()
    return airportArr

def GetAllAvaiableAirport():
    allAirports = GetAllAirportName()

def GetRandomAirport():
    allAirportName = GetAllAirportName()
    return random.choice(allAirportName)

def CreateAvailableList():
    folder = 'data'
    fileName = "airportList.csv"
    filePath = os.path.join(folder, fileName)
    # Create file if not exist
    if not os.path.exists(filePath):
        open(filePath, 'w').close()
    else:
        open(filePath, 'w').close()

    allAirportName = GetAllAirportName()
    len(allAirportName)
    for i, name in enumerate(allAirportName):
        if not bIsDataEmpty(name):
            with open(filePath, 'a') as f:
                f.write(f'{name}\n')
                print(f'{i}: {name}')


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

