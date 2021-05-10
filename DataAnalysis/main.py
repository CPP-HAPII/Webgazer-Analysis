from AOI_tracker import *
from gazePoints import *
from saccade_calculations import *
import pandas as pd
import statistics

aoiCounters, aoi1Coords, aoi2Coords, aoi3Coords, aoi4Coords, aoi5Coords, aoi6Coords, notAoiCoords = get_AOI_Info('testGazePoints.csv', 'testAOI.csv')
numOfGazePoints, allCoordinates = get_gazePoints('testGazePoints.csv')

'''
    Storing page saccades into csv files
'''
print("Total gaze points/fixations on page: " + str(numOfGazePoints))
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
df.to_csv('pageSaccades.csv')

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
df.to_csv('pageStats.csv')



# stores the number of fixations there are in each AOI into a csv
df = pd.DataFrame(aoiCounters, index=[0])
df.to_csv('AOI fixations.csv')

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
df.to_csv('aoi1Saccades.csv')

# Stores AOI1 Stats into a csv
# AOI1 saccade statistics
aoi1SaccadeLengthMean = statistics.mean(aoi1Saccades)
aoi1SaccadeLengthSD = statistics.stdev(aoi1Saccades)

aoi1AbsSaccadeAngMean = statistics.mean(aoi1Abs)
aoi1AbsSaccadeAngSD = statistics.stdev(aoi1Abs)

aoi1RelSaccadeAngMean = statistics.mean(aoi1Rel)
aoi1RelSaccadeAngSD = statistics.stdev(aoi1Rel)

# storing AOI1 statistics into csv
aoi1Stats = {
    'Mean': [aoi1SaccadeLengthMean, aoi1AbsSaccadeAngMean, aoi1RelSaccadeAngMean],
    'Standard Deviation': [aoi1SaccadeLengthSD, aoi1AbsSaccadeAngSD, aoi1RelSaccadeAngSD]
}
df = pd.DataFrame(aoi1Stats)
df.index = ['AOI1 Saccade Length', 'AOI1 Absolute Saccade Angles', 'AOI1 Relative Saccade Angles']
df.to_csv('aoi1Stats.csv')



# STORES AOI2 SACCADE DATA INTO A CSV FILE
aoi2Data = [
    aoi2Saccades,
    aoi2Abs,
    aoi2Rel,
]
df = pd.DataFrame(aoi2Data)
df.index = ['AOI2 Saccade Lengths', 'AOI2 Absolute Saccade Angles', 'AOI2 Relative Saccade Angles']
df.to_csv('aoi2Saccades.csv')

# Stores AOI2 Stats into a csv
# AOI2 saccade statistics
aoi2SaccadeLengthMean = statistics.mean(aoi2Saccades)
aoi2SaccadeLengthSD = statistics.stdev(aoi2Saccades)

aoi2AbsSaccadeAngMean = statistics.mean(aoi2Abs)
aoi2AbsSaccadeAngSD = statistics.stdev(aoi2Abs)

aoi2RelSaccadeAngMean = statistics.mean(aoi2Rel)
aoi2RelSaccadeAngSD = statistics.stdev(aoi2Rel)

# storing AOI2 statistics into csv
aoi2Stats = {
    'Mean': [aoi2SaccadeLengthMean, aoi2AbsSaccadeAngMean, aoi2RelSaccadeAngMean],
    'Standard Deviation': [aoi2SaccadeLengthSD, aoi2AbsSaccadeAngSD, aoi2RelSaccadeAngSD]
}
df = pd.DataFrame(aoi2Stats)
df.index = ['AOI2 Saccade Length', 'AOI2 Absolute Saccade Angles', 'AOI2 Relative Saccade Angles']
df.to_csv('aoi2Stats.csv')



# STORES AOI3 SACCADE DATA INTO A CSV FILE
aoi3Data = [
    aoi3Saccades,
    aoi3Abs,
    aoi3Rel,
]
df = pd.DataFrame(aoi3Data)
df.index = ['AOI3 Saccade Lengths', 'AOI3 Absolute Saccade Angles', 'AOI3 Relative Saccade Angles']
df.to_csv('aoi3Saccades.csv')

# Stores AOI3 Stats into a csv
# AOI3 saccade statistics
aoi3SaccadeLengthMean = statistics.mean(aoi3Saccades)
aoi3SaccadeLengthSD = statistics.stdev(aoi3Saccades)

aoi3AbsSaccadeAngMean = statistics.mean(aoi3Abs)
aoi3AbsSaccadeAngSD = statistics.stdev(aoi3Abs)

aoi3RelSaccadeAngMean = statistics.mean(aoi3Rel)
aoi3RelSaccadeAngSD = statistics.stdev(aoi3Rel)

# storing AOI3 statistics into csv
aoi3Stats = {
    'Mean': [aoi3SaccadeLengthMean, aoi3AbsSaccadeAngMean, aoi3RelSaccadeAngMean],
    'Standard Deviation': [aoi3SaccadeLengthSD, aoi3AbsSaccadeAngSD, aoi3RelSaccadeAngSD]
}
df = pd.DataFrame(aoi3Stats)
df.index = ['AOI3 Saccade Length', 'AOI3 Absolute Saccade Angles', 'AOI3 Relative Saccade Angles']
df.to_csv('aoi3Stats.csv')



# STORES AOI4 SACCADE DATA INTO A CSV FILE
aoi4Data = [
    aoi4Saccades,
    aoi4Abs,
    aoi4Rel,
]
df = pd.DataFrame(aoi4Data)
df.index = ['AOI4 Saccade Lengths', 'AOI4 Absolute Saccade Angles', 'AOI4 Relative Saccade Angles']
df.to_csv('aoi4Saccades.csv')

# Stores AOI4 Stats into a csv
# AOI4 saccade statistics
aoi4SaccadeLengthMean = statistics.mean(aoi4Saccades)
aoi4SaccadeLengthSD = statistics.stdev(aoi4Saccades)

aoi4AbsSaccadeAngMean = statistics.mean(aoi4Abs)
aoi4AbsSaccadeAngSD = statistics.stdev(aoi4Abs)

aoi4RelSaccadeAngMean = statistics.mean(aoi4Rel)
aoi4RelSaccadeAngSD = statistics.stdev(aoi4Rel)

# storing AOI4 statistics into csv
aoi4Stats = {
    'Mean': [aoi4SaccadeLengthMean, aoi4AbsSaccadeAngMean, aoi4RelSaccadeAngMean],
    'Standard Deviation': [aoi4SaccadeLengthSD, aoi4AbsSaccadeAngSD, aoi4RelSaccadeAngSD]
}
df = pd.DataFrame(aoi4Stats)
df.index = ['AOI4 Saccade Length', 'AOI4 Absolute Saccade Angles', 'AOI4 Relative Saccade Angles']
df.to_csv('aoi4Stats.csv')



# STORES AOI5 SACCADE DATA INTO A CSV FILE
aoi5Data = [
    aoi5Saccades,
    aoi5Abs,
    aoi5Rel,
]
df = pd.DataFrame(aoi5Data)
df.index = ['AOI5 Saccade Lengths', 'AOI5 Absolute Saccade Angles', 'AOI5 Relative Saccade Angles']
df.to_csv('aoi5Saccades.csv')

# Stores AOI5 Stats into a csv
# AOI5 saccade statistics
aoi5SaccadeLengthMean = statistics.mean(aoi5Saccades)
aoi5SaccadeLengthSD = statistics.stdev(aoi5Saccades)

aoi5AbsSaccadeAngMean = statistics.mean(aoi5Abs)
aoi5AbsSaccadeAngSD = statistics.stdev(aoi5Abs)

aoi5RelSaccadeAngMean = statistics.mean(aoi5Rel)
aoi5RelSaccadeAngSD = statistics.stdev(aoi5Rel)

# storing AOI5 statistics into csv
aoi5Stats = {
    'Mean': [aoi5SaccadeLengthMean, aoi5AbsSaccadeAngMean, aoi5RelSaccadeAngMean],
    'Standard Deviation': [aoi5SaccadeLengthSD, aoi5AbsSaccadeAngSD, aoi5RelSaccadeAngSD]
}
df = pd.DataFrame(aoi5Stats)
df.index = ['AOI5 Saccade Length', 'AOI5 Absolute Saccade Angles', 'AOI5 Relative Saccade Angles']
df.to_csv('aoi5Stats.csv')



# STORES AOI6 SACCADE DATA INTO A CSV FILE
aoi6Data = [
    aoi6Saccades,
    aoi6Abs,
    aoi6Rel,
]
df = pd.DataFrame(aoi6Data)
df.index = ['AOI6 Saccade Lengths', 'AOI6 Absolute Saccade Angles', 'AOI6 Relative Saccade Angles']
df.to_csv('aoi6Saccades.csv')

# Stores AOI6 Stats into a csv
# AOI6 saccade statistics
aoi6SaccadeLengthMean = statistics.mean(aoi6Saccades)
aoi6SaccadeLengthSD = statistics.stdev(aoi6Saccades)

aoi6AbsSaccadeAngMean = statistics.mean(aoi6Abs)
aoi6AbsSaccadeAngSD = statistics.stdev(aoi6Abs)

aoi6RelSaccadeAngMean = statistics.mean(aoi6Rel)
aoi6RelSaccadeAngSD = statistics.stdev(aoi6Rel)

# storing AOI6 statistics into csv
aoi6Stats = {
    'Mean': [aoi6SaccadeLengthMean, aoi6AbsSaccadeAngMean, aoi6RelSaccadeAngMean],
    'Standard Deviation': [aoi6SaccadeLengthSD, aoi6AbsSaccadeAngSD, aoi6RelSaccadeAngSD]
}
df = pd.DataFrame(aoi6Stats)
df.index = ['AOI6 Saccade Length', 'AOI6 Absolute Saccade Angles', 'AOI6 Relative Saccade Angles']
df.to_csv('aoi6Stats.csv')



# STORES NOT_AOI SACCADE DATA INTO A CSV FILE
notAoiData = [
    notAoiSaccades,
    notAoiAbs,
    notAoiRel,
]
df = pd.DataFrame(notAoiData)
df.index = ['NOT_AOI Saccade Lengths', 'NOT_AOI Absolute Saccade Angles', 'NOT_AOI Relative Saccade Angles']
df.to_csv('notAoiSaccades.csv')

# Stores NOT_AOI Stats into a csv
# NOT_AOI saccade statistics
notAoiSaccadeLengthMean = statistics.mean(notAoiSaccades)
notAoiSaccadeLengthSD = statistics.stdev(notAoiSaccades)

notAoiAbsSaccadeAngMean = statistics.mean(notAoiAbs)
notAoiAbsSaccadeAngSD = statistics.stdev(notAoiAbs)

notAoiRelSaccadeAngMean = statistics.mean(notAoiRel)
notAoiRelSaccadeAngSD = statistics.stdev(notAoiRel)

# storing NOT_AOI statistics into csv
notAoiStats = {
    'Mean': [notAoiSaccadeLengthMean, notAoiAbsSaccadeAngMean, notAoiRelSaccadeAngMean],
    'Standard Deviation': [notAoiSaccadeLengthSD, notAoiAbsSaccadeAngSD, notAoiRelSaccadeAngSD]
}
df = pd.DataFrame(notAoiStats)
df.index = ['NOT_AOI Saccade Length', 'NOT_AOI Absolute Saccade Angles', 'NOT_AOI Relative Saccade Angles']
df.to_csv('notAoiStats.csv')
