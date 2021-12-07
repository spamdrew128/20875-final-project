import pandas
import numpy as np

def avgFinder(start_day, data):
    day_vals = [[]]*7
    #day_vals = np.array(day_vals)

    for i in range(len(data)):
        day = (i + start_day) % 7
        day_vals[day].append(data[i])
    
    avgs = [np.mean(day) for day in day_vals]
    return avgs

def mseFinder(data1, data2):
    assert(len(data1) == len(data2))
    errors = [(data1[i] - data2[i])**2 for i in range(len(data1))]

    return np.mean(errors)

#section used to read and parse the file; sorts individual columns for easier manipulation later
bike_data_total = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')

day_of_week = bike_data_total.iloc[:, 1].values

#weather data
highTempF = np.array(bike_data_total.iloc[:, 2].values)
lowTempF = np.array(bike_data_total.iloc[:, 3].values)
Precip = np.array(bike_data_total.iloc[:, 4].values)

#Bridge data
Brooklyn = np.array(pandas.array(bike_data_total.iloc[:, 5].values))
Manhattan = np.array(pandas.array(bike_data_total.iloc[:, 6].values))
Williamsburg = np.array(pandas.array(bike_data_total.iloc[:, 7].values))
Queensboro = np.array(pandas.array(bike_data_total.iloc[:, 8].values))
TotalTravelers = np.array(pandas.array(bike_data_total.iloc[:, 9].values))
allBridgeData = [Brooklyn, Manhattan, Williamsburg, Queensboro]

#converts bridge data into integers
allBridgeTravelers = [[int(travelers.replace(',', '')) for travelers in bridge] for bridge in allBridgeData]



