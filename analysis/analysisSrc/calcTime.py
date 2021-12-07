import pandas as pd

def calc_avg_time(eyeGazeData_coords):
    avgTime = 0
    timeList = []
    if len(eyeGazeData_coords) >= 1:
        for i in range(0, len(eyeGazeData_coords)):
            timeList.append(eyeGazeData_coords[i][0])

        avgTime = sum(timeList) / len(timeList)

    return avgTime
