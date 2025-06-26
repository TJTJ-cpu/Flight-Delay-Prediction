from numpy import empty
import pandas as pd
import matplotlib.pyplot as plt
import random
import os

from pandas.io.common import file_path_to_url



def GetAllAirportName():
    filePath = "data/airportList.csv"
    if not os.path.exists(filePath):
        CreateAvailableList()
    df = pd.read_csv(filePath)
    return df


# def GetAirportID(name):


def GetRandomAirport():
    allAirportName = GetAllAirportName()
    return random.choice(allAirportName['name'].tolist())

def CreateAvailableList():
    folder = 'data'
    fileName = "airportList.csv"
    filePath = os.path.join(folder, fileName)
    # Create file if not exist
    if not os.path.exists(filePath):
        open(filePath, 'w').close()
    else:
        open(filePath, 'w').close()

    df = pd.read_csv("data/airports.csv")
    # get all unique name
    allAirportName = df['name'].drop_duplicates().tolist()
    # get all name with data
    validNames = [name for name in allAirportName if not bIsDataEmpty(name)]
    newDf = pd.DataFrame({'name': validNames})
    newDf.to_csv("data/airportList.csv", index=False)


def GetAirportData(airportName):
    df = pd.read_csv("data/airports.csv")
    flightsData = pd.read_csv("data/flights.csv")
    aiportInfo= df[df["name"].str.contains(airportName)]
    airportId = aiportInfo["airport_id"].values[0] # Fake Error Here
    airportData = flightsData[(flightsData["OriginAirportID"] == airportId) | 
                        (flightsData["DestAirportID"] == airportId)]
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

