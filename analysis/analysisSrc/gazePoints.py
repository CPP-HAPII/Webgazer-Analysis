import csv
import pandas as pd

def get_gazePoints(input_gazePoint_file):
    col_list1 = ['Time', 'X Coordinate', 'Y Coordinate']

    df1 = pd.read_csv(input_gazePoint_file, usecols=col_list1)

    # storing gaze point data
    timeList = []
    xCoordinatesList = []
    yCoordinatesList = []

    for time in df1['Time']:
        timeList.append(time)
    for x in df1['X Coordinate']:
        xCoordinatesList.append(x)
    for y in df1['Y Coordinate']:
        yCoordinatesList.append(y)

    # stores all the webgazer coordinates into x, y format
    allCoordinatesList = list(zip(xCoordinatesList, yCoordinatesList))
    # stores all eye gaze data in time, x, y format
    allEyeGazeData = list(zip(timeList, xCoordinatesList, yCoordinatesList))

    # gaze point coordinates counter
    allPointsCounter = 0
    for i in allCoordinatesList:
        allPointsCounter += 1

    return allPointsCounter, allCoordinatesList, allEyeGazeData
