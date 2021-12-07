import pandas
import numpy as np

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
for bridge in allBridgeData:
    tempVals = []
    for travelers in bridge:
        tempVals.append(int(travelers.replace(',', '')))

new = [[int(travelers.replace(',', '')) for travelers in bridge] for bridge in allBridgeData]


#print(type(Brooklyn[0]))
#print(Brooklyn[0])

print(new[0][0])


#def trendFinder():
