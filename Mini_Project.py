import pandas
import numpy as np

#section used to read and parse the file; sorts individual columns for easier manipulation later
bike_data_total = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')

day_of_week = bike_data_total.iloc[:, 1].values

#weather data
highTempF = np.array(bike_data_total.iloc[:, 2].values)
lowTempF = np.array(bike_data_total.iloc[:, 3].values)
Precip = np.array(bike_data_total.iloc[:, 4].values)

#Bridge data as Panda Series
BrooklynS = bike_data_total.iloc[:, 5]
ManhattanS = bike_data_total.iloc[:, 6].values
WilliamsburgS = bike_data_total.iloc[:, 7].values
QueensboroS = bike_data_total.iloc[:, 8].values
allBridgeDataS = [Brooklyn, Manhattan, Williamsburg, Queensboro]
TotalTravelersS = bike_data_total.iloc[:, 9].values

#Bridge data as Numpy Arrays

#converts bridge data into integers
for bridge in allBridgeData:
    for travelers in bridge:
        travelers = int(travelers.replace(',', ''))
        print(type(temp))

print(type(BrooklynDF[0]))

#1: which bridges should the sensors be installed on to get the best sense of total traffic
#open to ideas here, the way it will be written below is by taking the average of each data set, finding how many
#data points are higher than that and counting them, then choosing which three bridges have the highest count

#way 1
highTrafficBridges = []
for bridge in allBridgeData:
    highTrafficDays = 0
    AvgTravelers = np.average(bridge)
    for travelers in bridge:
        if travelers > AvgTravelers:
            highTrafficDays += 1
    highTrafficBridges.append(highTrafficDays)

#print(highTrafficBridges)

