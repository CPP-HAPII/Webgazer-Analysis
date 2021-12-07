import csv
import pandas as pd

def get_AOICoords_Info(input_gazePoint_file, input_aoiPositions_file):
    col_list1 = ['Time', 'X Coordinate', 'Y Coordinate']
    col_list2 = [
        'Left Position',
        'Right Position',
        'TopAOIPos1',
        'BotAOIPos1',
        'TopAOIPos2',
        'BotAOIPos2',
        'TopAOIPos3',
        'BotAOIPos3',
        'TopAOIPos4',
        'BotAOIPos4',
        'TopAOIPos5',
        'BotAOIPos5',
        'TopAOIPos6',
        'BotAOIPos6'
    ]

    df1 = pd.read_csv(input_gazePoint_file, usecols=col_list1)
    df2 = pd.read_csv(input_aoiPositions_file, usecols=col_list2)

    # get the left and right positions
    leftPos = df2.values[0][0]
    rightPos = df2.values[0][1]

    # storing gaze point data
    timeList = []
    xCoordinatesList = []
    yCoordinatesList = []

    # storing aoi position data
    topPositionsList = []
    botPositionsList = []

    for time in df1['Time']:
        timeList.append(time)
    for x in df1['X Coordinate']:
        xCoordinatesList.append(x)
    for y in df1['Y Coordinate']:
        yCoordinatesList.append(y)

    topPositionsList = [df2.values[0][2], df2.values[0][4], df2.values[0][6], df2.values[0][8], df2.values[0][10], df2.values[0][12]]
    botPositionsList = [df2.values[0][3], df2.values[0][5], df2.values[0][7], df2.values[0][9], df2.values[0][11], df2.values[0][13]]

    # lists for holding coordinates in time, x, y format for each AOI
    aoi1Coordinates = []
    aoi2Coordinates = []
    aoi3Coordinates = []
    aoi4Coordinates = []
    aoi5Coordinates = []
    aoi6Coordinates = []
    notAoiCoordinates = []

    lookDirection = None
    aoi1Counter, aoi2Counter, aoi3Counter = 0, 0, 0
    aoi4Counter, aoi5Counter, aoi6Counter = 0, 0, 0
    notAoiCounter = 0

    for i in range(0, len(xCoordinatesList)):
        if (xCoordinatesList[i] >= leftPos and xCoordinatesList[i] <= rightPos):
            if (yCoordinatesList[i] >= topPositionsList[0] and yCoordinatesList[i] <= botPositionsList[0] and lookDirection != 'AOI1'):
                lookDirection = 'AOI1'
                aoi1Coordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

                aoi1Counter += 1
            elif (yCoordinatesList[i] >= topPositionsList[1] and yCoordinatesList[i] <= botPositionsList[1] and lookDirection != 'AOI2'):
                lookDirection = 'AOI2'
                aoi2Coordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

                aoi2Counter += 1
            elif (yCoordinatesList[i] >= topPositionsList[2] and yCoordinatesList[i] <= botPositionsList[2] and lookDirection != 'AOI3'):
                lookDirection = 'AOI3'
                aoi3Coordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

                aoi3Counter += 1
            elif (yCoordinatesList[i] >= topPositionsList[3] and yCoordinatesList[i] <= botPositionsList[3] and lookDirection != 'AOI4'):
                lookDirection = 'AOI4'
                aoi4Coordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

                aoi4Counter += 1
            elif (yCoordinatesList[i] >= topPositionsList[4] and yCoordinatesList[i] <= botPositionsList[4] and lookDirection != 'AOI5'):
                lookDirection = 'AOI5'
                aoi5Coordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

                aoi5Counter += 1
            elif (yCoordinatesList[i] >= topPositionsList[5] and yCoordinatesList[i] <= botPositionsList[5] and lookDirection != 'AOI6'):
                lookDirection = 'AOI6'
                aoi6Coordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

                aoi6Counter += 1
            else:
                lookDirection = 'NOT_AOI'
                notAoiCoordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

                notAoiCounter += 1
        else:
            lookDirection = 'NOT_AOI'
            notAoiCoordinates.append([timeList[i], xCoordinatesList[i], yCoordinatesList[i]])

            notAoiCounter += 1

    aoiCounterDict = {
        "AOI1": aoi1Counter,
        "AOI2": aoi2Counter,
        "AOI3": aoi3Counter,
        "AOI4": aoi4Counter,
        "AOI5": aoi5Counter,
        "AOI6": aoi6Counter,
        "NOT_AOI": notAoiCounter
    }

    return aoiCounterDict, aoi1Coordinates, aoi2Coordinates, aoi3Coordinates, aoi4Coordinates, aoi5Coordinates, aoi6Coordinates, notAoiCoordinates
