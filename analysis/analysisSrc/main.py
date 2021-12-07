from AOI_tracker import *
from gazePoints import *
from saccade_calculations import *
import pandas as pd
import statistics

for i in range(1, 31):
    aoiCounters, aoi1Coords, aoi2Coords, aoi3Coords, aoi4Coords, aoi5Coords, aoi6Coords, notAoiCoords = get_AOI_Info('../user5/user5Pages/page{}.csv'.format(i), '../user5/user5AOIPages/aoipage{}.csv'.format(i))
    numOfGazePoints, allCoordinates, allEyeGaze = get_gazePoints('../user5/user5Pages/page{}.csv'.format(i))

    '''
        Storing page saccades into csv files
    '''
    print("Total gaze points/fixations on page {}: ".format(i) + str(numOfGazePoints))
    print()

    # page saccade data
    saccadeLengthsOfPage = saccade_length(allCoordinates)
    absSaccadeAnglesOfPage = abs_saccade_angle(allCoordinates)
    relSaccadeAnglesOfPage = rel_saccade_angle(allCoordinates)

    # storing page saccades into csv
    pageData = [
        saccadeLengthsOfPage,
        absSaccadeAnglesOfPage,
        relSaccadeAnglesOfPage,
    ]
    df = pd.DataFrame(pageData)
    df.index = ['Page Saccade Lengths', 'Page Absolute Saccade Angles', 'Page Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}Saccades.csv'.format(i, i))

    # Page saccade statistics
    pageSaccadeLengthMean = statistics.mean(saccadeLengthsOfPage)
    pageSaccadeLengthSD = statistics.stdev(saccadeLengthsOfPage)

    pageAbsSaccadeAngMean = statistics.mean(absSaccadeAnglesOfPage)
    pageAbsSaccadeAngSD = statistics.stdev(absSaccadeAnglesOfPage)

    pageRelSaccadeAngMean = statistics.mean(relSaccadeAnglesOfPage)
    pageRelSaccadeAngSD = statistics.stdev(relSaccadeAnglesOfPage)

    # storing page statistics into csv
    pageStats = {
        'Mean': [pageSaccadeLengthMean, pageAbsSaccadeAngMean, pageRelSaccadeAngMean],
        'Standard Deviation': [pageSaccadeLengthSD, pageAbsSaccadeAngSD, pageRelSaccadeAngSD]
    }
    df = pd.DataFrame(pageStats)
    df.index = ['Page Saccade Length', 'Page Absolute Saccade Angles', 'Page Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}Stats.csv'.format(i, i))



    # stores the number of fixations there are in each AOI into a csv
    df = pd.DataFrame(aoiCounters, index=[0])
    df.to_csv('../user5/user5Analysis/page{}/page{}AOI_fixations.csv'.format(i, i))

    # AOI Saccade Lengths
    aoi1Saccades = saccade_length(aoi1Coords)
    aoi2Saccades = saccade_length(aoi2Coords)
    aoi3Saccades = saccade_length(aoi3Coords)
    aoi4Saccades = saccade_length(aoi4Coords)
    aoi5Saccades = saccade_length(aoi5Coords)
    aoi6Saccades = saccade_length(aoi6Coords)
    notAoiSaccades = saccade_length(notAoiCoords)


    # AOI Absolute saccade angles
    aoi1Abs = abs_saccade_angle(aoi1Coords)
    aoi2Abs = abs_saccade_angle(aoi2Coords)
    aoi3Abs = abs_saccade_angle(aoi3Coords)
    aoi4Abs = abs_saccade_angle(aoi4Coords)
    aoi5Abs = abs_saccade_angle(aoi5Coords)
    aoi6Abs = abs_saccade_angle(aoi6Coords)
    notAoiAbs = abs_saccade_angle(notAoiCoords)


    # AOI Relative Saccade Angles
    aoi1Rel = rel_saccade_angle(aoi1Coords)
    aoi2Rel = rel_saccade_angle(aoi2Coords)
    aoi3Rel = rel_saccade_angle(aoi3Coords)
    aoi4Rel = rel_saccade_angle(aoi4Coords)
    aoi5Rel = rel_saccade_angle(aoi5Coords)
    aoi6Rel = rel_saccade_angle(aoi6Coords)
    notAoiRel = rel_saccade_angle(notAoiCoords)


    '''
        Storing AOI Saccades into their respective csv files
    '''
    # STORES AOI1 SACCADE DATA INTO A CSV FILE
    aoi1Data = [
        aoi1Saccades,
        aoi1Abs,
        aoi1Rel,
    ]
    df = pd.DataFrame(aoi1Data)
    df.index = ['AOI1 Saccade Lengths', 'AOI1 Absolute Saccade Angles', 'AOI1 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi1Saccades.csv'.format(i, i))

    # Stores AOI1 Stats into a csv
    # AOI1 saccade statistics
    if len(aoi1Saccades) <= 1:
        aoi1SaccadeLengthMean = 0
        aoi1SaccadeLengthSD = 0
    else:
        aoi1SaccadeLengthMean = statistics.mean(aoi1Saccades)
        aoi1SaccadeLengthSD = statistics.stdev(aoi1Saccades)

    if len(aoi1Abs) <= 1:
        aoi1AbsSaccadeAngMean = 0
        aoi1AbsSaccadeAngSD = 0
    else:
        aoi1AbsSaccadeAngMean = statistics.mean(aoi1Abs)
        aoi1AbsSaccadeAngSD = statistics.stdev(aoi1Abs)

    if len(aoi1Rel) <= 1:
        aoi1RelSaccadeAngMean = 0
        aoi1RelSaccadeAngSD = 0
    else:
        aoi1RelSaccadeAngMean = statistics.mean(aoi1Rel)
        aoi1RelSaccadeAngSD = statistics.stdev(aoi1Rel)


    # storing AOI1 statistics into csv
    aoi1Stats = {
        'Mean': [aoi1SaccadeLengthMean, aoi1AbsSaccadeAngMean, aoi1RelSaccadeAngMean],
        'Standard Deviation': [aoi1SaccadeLengthSD, aoi1AbsSaccadeAngSD, aoi1RelSaccadeAngSD]
    }
    df = pd.DataFrame(aoi1Stats)
    df.index = ['AOI1 Saccade Length', 'AOI1 Absolute Saccade Angles', 'AOI1 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi1Stats.csv'.format(i, i))



    # STORES AOI2 SACCADE DATA INTO A CSV FILE
    aoi2Data = [
        aoi2Saccades,
        aoi2Abs,
        aoi2Rel,
    ]
    df = pd.DataFrame(aoi2Data)
    df.index = ['AOI2 Saccade Lengths', 'AOI2 Absolute Saccade Angles', 'AOI2 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi2Saccades.csv'.format(i, i))

    # Stores AOI2 Stats into a csv
    # AOI2 saccade statistics
    if len(aoi2Saccades) <= 1:
        aoi2SaccadeLengthSD = 0
        aoi2SaccadeLengthMean = 0
    else:
        aoi2SaccadeLengthMean = statistics.mean(aoi2Saccades)
        aoi2SaccadeLengthSD = statistics.stdev(aoi2Saccades)

    if len(aoi2Abs) <= 1:
        aoi2AbsSaccadeAngMean = 0
        aoi2AbsSaccadeAngSD = 0
    else:
        aoi2AbsSaccadeAngMean = statistics.mean(aoi2Abs)
        aoi2AbsSaccadeAngSD = statistics.stdev(aoi2Abs)

    if len(aoi2Rel) <= 1:
        aoi2RelSaccadeAngSD = 0
        aoi2RelSaccadeAngMean = 0
    else:
        aoi2RelSaccadeAngMean = statistics.mean(aoi2Rel)
        aoi2RelSaccadeAngSD = statistics.stdev(aoi2Rel)

    # storing AOI2 statistics into csv
    aoi2Stats = {
        'Mean': [aoi2SaccadeLengthMean, aoi2AbsSaccadeAngMean, aoi2RelSaccadeAngMean],
        'Standard Deviation': [aoi2SaccadeLengthSD, aoi2AbsSaccadeAngSD, aoi2RelSaccadeAngSD]
    }
    df = pd.DataFrame(aoi2Stats)
    df.index = ['AOI2 Saccade Length', 'AOI2 Absolute Saccade Angles', 'AOI2 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi2Stats.csv'.format(i, i))



    # STORES AOI3 SACCADE DATA INTO A CSV FILE
    aoi3Data = [
        aoi3Saccades,
        aoi3Abs,
        aoi3Rel,
    ]
    df = pd.DataFrame(aoi3Data)
    df.index = ['AOI3 Saccade Lengths', 'AOI3 Absolute Saccade Angles', 'AOI3 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi3Saccades.csv'.format(i, i))

    # Stores AOI3 Stats into a csv
    # AOI3 saccade statistics
    if len(aoi3Saccades) <= 1:
        aoi3SaccadeLengthMean = 0
        aoi3SaccadeLengthSD = 0
    else:
        aoi3SaccadeLengthMean = statistics.mean(aoi3Saccades)
        aoi3SaccadeLengthSD = statistics.stdev(aoi3Saccades)

    if len(aoi3Abs) <= 1:
        aoi3AbsSaccadeAngMean = 0
        aoi3AbsSaccadeAngSD = 0
    else:
        aoi3AbsSaccadeAngMean = statistics.mean(aoi3Abs)
        aoi3AbsSaccadeAngSD = statistics.stdev(aoi3Abs)

    if len(aoi3Rel) <= 1:
        aoi3RelSaccadeAngMean = 0
        aoi3RelSaccadeAngSD = 0
    else:
        aoi3RelSaccadeAngMean = statistics.mean(aoi3Rel)
        aoi3RelSaccadeAngSD = statistics.stdev(aoi3Rel)

    # storing AOI3 statistics into csv
    aoi3Stats = {
        'Mean': [aoi3SaccadeLengthMean, aoi3AbsSaccadeAngMean, aoi3RelSaccadeAngMean],
        'Standard Deviation': [aoi3SaccadeLengthSD, aoi3AbsSaccadeAngSD, aoi3RelSaccadeAngSD]
    }
    df = pd.DataFrame(aoi3Stats)
    df.index = ['AOI3 Saccade Length', 'AOI3 Absolute Saccade Angles', 'AOI3 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi3Stats.csv'.format(i, i))



    # STORES AOI4 SACCADE DATA INTO A CSV FILE
    aoi4Data = [
        aoi4Saccades,
        aoi4Abs,
        aoi4Rel,
    ]
    df = pd.DataFrame(aoi4Data)
    df.index = ['AOI4 Saccade Lengths', 'AOI4 Absolute Saccade Angles', 'AOI4 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi4Saccades.csv'.format(i, i))

    # Stores AOI4 Stats into a csv
    # AOI4 saccade statistics

    if len(aoi4Saccades) <= 1:
        aoi4SaccadeLengthMean = 0
        aoi4SaccadeLengthSD = 0
    else:
        aoi4SaccadeLengthMean = statistics.mean(aoi4Saccades)
        aoi4SaccadeLengthSD = statistics.stdev(aoi4Saccades)

    if len(aoi4Abs) <= 1:
        aoi4AbsSaccadeAngMean = 0
        aoi4AbsSaccadeAngSD = 0
    else:
        aoi4AbsSaccadeAngMean = statistics.mean(aoi4Abs)
        aoi4AbsSaccadeAngSD = statistics.stdev(aoi4Abs)

    if len(aoi4Rel) <= 1:
        aoi4RelSaccadeAngMean = 0
        aoi4RelSaccadeAngSD = 0
    else:
        aoi4RelSaccadeAngMean = statistics.mean(aoi4Rel)
        aoi4RelSaccadeAngSD = statistics.stdev(aoi4Rel)

    # storing AOI4 statistics into csv
    aoi4Stats = {
        'Mean': [aoi4SaccadeLengthMean, aoi4AbsSaccadeAngMean, aoi4RelSaccadeAngMean],
        'Standard Deviation': [aoi4SaccadeLengthSD, aoi4AbsSaccadeAngSD, aoi4RelSaccadeAngSD]
    }
    df = pd.DataFrame(aoi4Stats)
    df.index = ['AOI4 Saccade Length', 'AOI4 Absolute Saccade Angles', 'AOI4 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi4Stats.csv'.format(i, i))



    # STORES AOI5 SACCADE DATA INTO A CSV FILE
    aoi5Data = [
        aoi5Saccades,
        aoi5Abs,
        aoi5Rel,
    ]
    df = pd.DataFrame(aoi5Data)
    df.index = ['AOI5 Saccade Lengths', 'AOI5 Absolute Saccade Angles', 'AOI5 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi5Saccades.csv'.format(i, i))

    # Stores AOI5 Stats into a csv
    # AOI5 saccade statistics
    if len(aoi5Saccades) <= 1:
        aoi5SaccadeLengthMean = 0
        aoi5SaccadeLengthSD = 0
    else:
        aoi5SaccadeLengthMean = statistics.mean(aoi5Saccades)
        aoi5SaccadeLengthSD = statistics.stdev(aoi5Saccades)

    if len(aoi5Abs) <= 1:
        aoi5AbsSaccadeAngMean = 0
        aoi5AbsSaccadeAngSD = 0
    else:
        aoi5AbsSaccadeAngMean = statistics.mean(aoi5Abs)
        aoi5AbsSaccadeAngSD = statistics.stdev(aoi5Abs)

    if len(aoi5Rel) <= 1:
        aoi5RelSaccadeAngMean = 0
        aoi5RelSaccadeAngSD = 0
    else:
        aoi5RelSaccadeAngMean = statistics.mean(aoi5Rel)
        aoi5RelSaccadeAngSD = statistics.stdev(aoi5Rel)

    # storing AOI5 statistics into csv
    aoi5Stats = {
        'Mean': [aoi5SaccadeLengthMean, aoi5AbsSaccadeAngMean, aoi5RelSaccadeAngMean],
        'Standard Deviation': [aoi5SaccadeLengthSD, aoi5AbsSaccadeAngSD, aoi5RelSaccadeAngSD]
    }
    df = pd.DataFrame(aoi5Stats)
    df.index = ['AOI5 Saccade Length', 'AOI5 Absolute Saccade Angles', 'AOI5 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi5Stats.csv'.format(i, i))



    # STORES AOI6 SACCADE DATA INTO A CSV FILE
    aoi6Data = [
        aoi6Saccades,
        aoi6Abs,
        aoi6Rel,
    ]
    df = pd.DataFrame(aoi6Data)
    df.index = ['AOI6 Saccade Lengths', 'AOI6 Absolute Saccade Angles', 'AOI6 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi6Saccades.csv'.format(i, i))

    # Stores AOI6 Stats into a csv
    # AOI6 saccade statistics
    if len(aoi6Saccades) <= 1:
        aoi6SaccadeLengthMean = 0
        aoi6SaccadeLengthSD = 0
    else:
        aoi6SaccadeLengthMean = statistics.mean(aoi6Saccades)
        aoi6SaccadeLengthSD = statistics.stdev(aoi6Saccades)

    if len(aoi6Abs) <= 1:
        aoi6AbsSaccadeAngMean = 0
        aoi6AbsSaccadeAngSD = 0
    else:
        aoi6AbsSaccadeAngMean = statistics.mean(aoi6Abs)
        aoi6AbsSaccadeAngSD = statistics.stdev(aoi6Abs)

    if len(aoi6Rel) <= 1:
        aoi6RelSaccadeAngMean = 0
        aoi6RelSaccadeAngSD = 0
    else:
        aoi6RelSaccadeAngMean = statistics.mean(aoi6Rel)
        aoi6RelSaccadeAngSD = statistics.stdev(aoi6Rel)

    # storing AOI6 statistics into csv
    aoi6Stats = {
        'Mean': [aoi6SaccadeLengthMean, aoi6AbsSaccadeAngMean, aoi6RelSaccadeAngMean],
        'Standard Deviation': [aoi6SaccadeLengthSD, aoi6AbsSaccadeAngSD, aoi6RelSaccadeAngSD]
    }
    df = pd.DataFrame(aoi6Stats)
    df.index = ['AOI6 Saccade Length', 'AOI6 Absolute Saccade Angles', 'AOI6 Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_aoi6Stats.csv'.format(i, i))



    # STORES NOT_AOI SACCADE DATA INTO A CSV FILE
    notAoiData = [
        notAoiSaccades,
        notAoiAbs,
        notAoiRel,
    ]
    df = pd.DataFrame(notAoiData)
    df.index = ['NOT_AOI Saccade Lengths', 'NOT_AOI Absolute Saccade Angles', 'NOT_AOI Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_notAOISaccades.csv'.format(i, i))

    # Stores NOT_AOI Stats into a csv
    # NOT_AOI saccade statistics
    if len(notAoiSaccades) <= 1:
        notAoiSaccadeLengthMean = 0
        notAoiSaccadeLengthSD = 0
    else:
        notAoiSaccadeLengthMean = statistics.mean(notAoiSaccades)
        notAoiSaccadeLengthSD = statistics.stdev(notAoiSaccades)

    if len(notAoiAbs) <= 1:
        notAoiAbsSaccadeAngMean = 0
        notAoiAbsSaccadeAngSD = 0
    else:
        notAoiAbsSaccadeAngMean = statistics.mean(notAoiAbs)
        notAoiAbsSaccadeAngSD = statistics.stdev(notAoiAbs)

    if len(notAoiRel) <= 1:
        notAoiRelSaccadeAngMean = 0
        notAoiRelSaccadeAngSD = 0
    else:
        notAoiRelSaccadeAngMean = statistics.mean(notAoiRel)
        notAoiRelSaccadeAngSD = statistics.stdev(notAoiRel)

    # storing NOT_AOI statistics into csv
    notAoiStats = {
        'Mean': [notAoiSaccadeLengthMean, notAoiAbsSaccadeAngMean, notAoiRelSaccadeAngMean],
        'Standard Deviation': [notAoiSaccadeLengthSD, notAoiAbsSaccadeAngSD, notAoiRelSaccadeAngSD]
    }
    df = pd.DataFrame(notAoiStats)
    df.index = ['NOT_AOI Saccade Length', 'NOT_AOI Absolute Saccade Angles', 'NOT_AOI Relative Saccade Angles']
    df.to_csv('../user5/user5Analysis/page{}/page{}_notAOIStats.csv'.format(i, i))
