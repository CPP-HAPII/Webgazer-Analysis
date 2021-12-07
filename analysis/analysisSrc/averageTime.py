from AOI_coords_tracker import *
from gazePoints import *
from calcTime import *
import pandas as pd

for i in range(1, 31):
    aoiCounters, aoi1Coords, aoi2Coords, aoi3Coords, aoi4Coords, aoi5Coords, aoi6Coords, notAoiCoords = get_AOICoords_Info('../user5/user5Pages/page{}.csv'.format(i), '../user5/user5AOIPages/aoipage{}.csv'.format(i))
    numOfGazePoints, allCoordinates, allEyeGaze = get_gazePoints('../user5/user5Pages/page{}.csv'.format(i))
    pageAvgTime, aoi1AvgTime, aoi2AvgTime, aoi3AvgTime, aoi4AvgTime, aoi5AvgTime, aoi6AvgTime = 0, 0, 0, 0, 0, 0, 0

    '''
        Storing average time spent per page into CSV
    '''
    print("Total gaze points/fixations on page {}: ".format(i) + str(numOfGazePoints))
    print()

    pageAvgTime = calc_avg_time(allEyeGaze)
    aoi1AvgTime = calc_avg_time(aoi1Coords)
    aoi2AvgTime = calc_avg_time(aoi2Coords)
    aoi3AvgTime = calc_avg_time(aoi3Coords)
    aoi4AvgTime = calc_avg_time(aoi4Coords)
    aoi5AvgTime = calc_avg_time(aoi5Coords)
    aoi6AvgTime = calc_avg_time(aoi6Coords)
    notAoiAvgTime = calc_avg_time(notAoiCoords)

    avgTimeData = [
        pageAvgTime,
        aoi1AvgTime,
        aoi2AvgTime,
        aoi3AvgTime,
        aoi4AvgTime,
        aoi5AvgTime,
        aoi6AvgTime,
        notAoiAvgTime
    ]

    avgTimeColumns = [
        'Overall page average time',
        'AOI 1 average time',
        'AOI 2 average time',
        'AOI 3 average time',
        'AOI 4 average time',
        'AOI 5 average time',
        'AOI 6 average time',
        'Not AOI average time'
    ]

    df = pd.DataFrame([avgTimeData], columns=avgTimeColumns)
    df.to_csv('../user5/user5Analysis/page{}/page{}_avgTimes.csv'.format(i, i), index=False)
