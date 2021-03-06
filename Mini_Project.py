import pandas
import numpy as np
import re
from functools import reduce
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#functions for part 1
def avgFinder(start_day, data):
    day_vals = [0]*7
    day_counts = [0]*7

    for i in range(len(data)):
        day = (i + start_day) % 7
        day_vals[day] += data[i]
        day_counts[day] += 1
    
    avgs = [0]*7
    for i in range(7):
        avgs[i] = day_vals[i] / day_counts[i]        
    
    return avgs

def mseFinder(data1, data2):
    assert(len(data1) == len(data2))
    errors = [(data1[i] - data2[i])**2 for i in range(len(data1))]

    return np.mean(errors)

#functions for part 2
def leastSquares(X, y):
    X = np.array(X)
    y = np.array(y)

    B = np.linalg.inv(X.T @ X) @ X.T @ y
    
    return B

def precipSorter(data):
    snow = re.compile("\d+\.\d+\s\(S\)")
    traces = re.compile("T")
    cleanedData = []
    indices = []

    for values in data:
        if snow.search(values):
            indices.append(list(data).index(values))
            values = snow.sub(values, "0")
        elif traces.search(values):
            values = traces.sub(values, "0.001")
        cleanedData.append(float(values))

    return np.array(cleanedData), indices

def traveler_yhat(coeffs, features):
    y_hat = features[0]*coeffs[0] + features[1]*coeffs[1] + features[2]*coeffs[2] + coeffs[3]

    return y_hat

#functions for part 3
def precip_to_binary(Precip, boundary=0.1):
    binary = [0 if val <= boundary else 1 for val in Precip]

    return np.array(binary)

#section used to read and parse the file; sorts individual columns for easier manipulation later
bike_data_total = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')

columnNames = bike_data_total.columns
bridgeNames = columnNames[5:9]

day_of_week = bike_data_total.iloc[:, 1].values

#weather data
highTempF = np.array(pandas.array(bike_data_total.iloc[:, 2].values))
lowTempF = np.array(pandas.array(bike_data_total.iloc[:, 3].values))
Precip = np.array(pandas.array(bike_data_total.iloc[:, 4].values))

#Bridge data
Brooklyn = np.array(pandas.array(bike_data_total.iloc[:, 5].values))
Manhattan = np.array(pandas.array(bike_data_total.iloc[:, 6].values))
Williamsburg = np.array(pandas.array(bike_data_total.iloc[:, 7].values))
Queensboro = np.array(pandas.array(bike_data_total.iloc[:, 8].values))
TotalTravelers = np.array(pandas.array(bike_data_total.iloc[:, 9].values))
allBridgeData = [Brooklyn, Manhattan, Williamsburg, Queensboro]

#converts purely numeric data into floats
allBridgeTravelers = [[float(travelers.replace(',', '')) for travelers in bridge] for bridge in allBridgeData]
TotalTravelers = [float(travelers.replace(',', '')) for travelers in TotalTravelers]
#highTempF = [float(temp.replace(',', '')) for temp in highTempF]
#lowTempF = [float(temp.replace(',', '')) for temp in lowTempF]


#PROBLEM 1
MSEs = []

for i in range(len(allBridgeTravelers)):
    travers_copy = allBridgeTravelers.copy()
    travers_copy.remove(travers_copy[i])
    cross_val = reduce(lambda x, y:	np.array(x) + np.array(y), travers_copy)

    MSEs.append(mseFinder(avgFinder(4, TotalTravelers),  avgFinder(4, cross_val)))


name_index = MSEs.index(min(MSEs))
#print("The {} bridge should not have sensors installed.".format(bridgeNames[name_index]))

#PROBLEM 2
Precip, Indices = precipSorter(Precip)
#print(type(Precip))

#removing snow values
for i in Indices:
    highTempF = np.delete(highTempF, i)
    lowTempF = np.delete(lowTempF, i)
    Precip = np.delete(Precip, i)
    y_true = np.delete(TotalTravelers, i)

X = np.array([highTempF, lowTempF, Precip, np.ones(len(highTempF))])
X = X.T
X = np.array([[float(val) for val in row] for row in X])

#print(X[0])

coeffs = leastSquares(X, y_true)
y_hat = [traveler_yhat(coeffs, [highTempF[i], lowTempF[i], Precip[i]]) for i in range(len(highTempF))]

r2 = r2_score(y_true, y_hat)
#print(coeffs)
#print(r2)

#PROBLEM 3
logreg = LogisticRegression()
x_train = y_true.reshape(-1, 1)
y_train = precip_to_binary(Precip)

logreg.fit(x_train, y_train)
y_pred = logreg.predict(x_train)

acc = metrics.accuracy_score(y_train, y_pred)
print(acc)
#print(logreg.get_params())
prob_of_rain = logreg.predict_proba(np.array(11000).reshape(-1, 1))[0][1]
