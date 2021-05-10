import csv
import pandas as pd

def get_gazePoints(input_gazePoint_file):
    col_list1 = ['0', '1', '2']

    df1 = pd.read_csv(input_gazePoint_file, usecols=col_list1)

    # storing gaze point data
    timeList = []
    xCoordinatesList = []
    yCoordinatesList = []

    for time in df1['0']:
        timeList.append(time)
    for x in df1['1']:
        xCoordinatesList.append(x)
    for y in df1['2']:
        yCoordinatesList.append(y)

    # stores all the webgazer coordinates into x, y format
    allCoordinatesList = list(zip(xCoordinatesList, yCoordinatesList))

    # gaze point coordinates counter
    allPointsCounter = 0
    for i in allCoordinatesList:
        allPointsCounter += 1

    return allPointsCounter, allCoordinatesList
