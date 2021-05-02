from AOI_tracker import *
from saccades import *

aoiCounters, aoi1Coords, aoi2Coords, aoi3Coords, aoi4Coords, aoi5Coords, aoi6Coords, notAoiCoords = get_AOI_Info('testGazePoints.csv', 'testAOI.csv')

print("AOI counters: " + str(aoiCounters))
print()


def saccade_length(aoiCoords):
    """
    Get the saccade length

    # Arguments
    cur_coords  -> [x, y] coordinates of the current point
    prev_coords -. [x, y] coordinates of the previous point
    """
    aoi_saccadeLengthList = []

    if len(aoiCoords) >= 2:
        for i in range(1, len(aoiCoords)):
            aoi_saccadeLengthList.append(calc_saccade_length(aoiCoords[i], aoiCoords[i-1]))


    return aoi_saccadeLengthList

def abs_saccade_angle(aoiCoords, useDegrees=True):
    """
    Calculate the absolute angle of 2 fixations using atan2
    # ARGUMENTS
    cur_coords  -> Current coordinates in [x, y] form
    prev_coords -> Previous coordinates in [x, y] form
    use_degrees -> True to return in degrees, False to return in radians
    """
    aoi_absSaccadeAngleList = []

    if len(aoiCoords) >= 2:
        for i in range(1, len(aoiCoords)):
            aoi_absSaccadeAngleList.append(calc_abs_angle(aoiCoords[i], aoiCoords[i-1], useDegrees))


    return aoi_absSaccadeAngleList

def rel_saccade_angle(aoiCoords, useDegrees=True):
    aoi_relSaccadeAngleList = []

    if len(aoiCoords) >= 3:
        for i in range(2, len(aoiCoords)):
            aoi_relSaccadeAngleList.append(calc_rel_angle(aoiCoords[i-1], aoiCoords[i-2], aoiCoords[i], useDegrees))

    return aoi_relSaccadeAngleList


print("================SACCADE LENGTHS==================")
aoi1Saccades = saccade_length(aoi1Coords)
print("AOI1 Saccades: " + str(aoi1Saccades))
print()

aoi2Saccades = saccade_length(aoi2Coords)
print("AOI2 Saccades: " + str(aoi2Saccades))
print()

aoi3Saccades = saccade_length(aoi3Coords)
print("AOI3 Saccades: " + str(aoi3Saccades))
print()

aoi4Saccades = saccade_length(aoi4Coords)
print("AOI4 Saccades: " + str(aoi4Saccades))
print()

aoi5Saccades = saccade_length(aoi5Coords)
print("AOI5 Saccades: " + str(aoi5Saccades))
print()

aoi6Saccades = saccade_length(aoi6Coords)
print("AOI6 Saccades: " + str(aoi6Saccades))
print()

notAoiSaccades = saccade_length(notAoiCoords)
print("NOT_AOI Saccades: " + str(notAoiSaccades))
print("\n\n")


print("===============ABSOLUTE SACCADE ANGLES=================")
aoi1Abs = abs_saccade_angle(aoi1Coords)
print("AOI1 Absolute Saccade Angles: " + str(aoi1Abs))
print()

aoi2Abs = abs_saccade_angle(aoi2Coords)
print("AOI2 Absolute Saccade Angles: " + str(aoi2Abs))
print()

aoi3Abs = abs_saccade_angle(aoi3Coords)
print("AOI3 Absolute Saccade Angles: " + str(aoi3Abs))
print()

aoi4Abs = abs_saccade_angle(aoi4Coords)
print("AOI4 Absolute Saccade Angles: " + str(aoi4Abs))
print()

aoi5Abs = abs_saccade_angle(aoi5Coords)
print("AOI5 Absolute Saccade Angles: " + str(aoi5Abs))
print()

aoi6Abs = abs_saccade_angle(aoi6Coords)
print("AOI6 Absolute Saccade Angles: " + str(aoi6Abs))
print()

notAoiAbs = abs_saccade_angle(notAoiCoords)
print("NOT_AOI Absolute Saccade Angles: " + str(notAoiAbs))
print("\n\n")


print("===============RELATIVE SACCADE ANGLES=================")
aoi1Rel = rel_saccade_angle(aoi1Coords)
print("AOI1 Relative Saccade Angles: " + str(aoi1Rel))
print()

aoi2Rel = rel_saccade_angle(aoi2Coords)
print("AOI2 Relative Saccade Angles: " + str(aoi2Rel))
print()

aoi3Rel = rel_saccade_angle(aoi3Coords)
print("AOI3 Relative Saccade Angles: " + str(aoi3Rel))
print()

aoi4Rel = rel_saccade_angle(aoi4Coords)
print("AOI4 Relative Saccade Angles: " + str(aoi4Rel))
print()

aoi5Rel = rel_saccade_angle(aoi5Coords)
print("AOI5 Relative Saccade Angles: " + str(aoi5Rel))
print()

aoi6Rel = rel_saccade_angle(aoi6Coords)
print("AOI6 Relative Saccade Angles: " + str(aoi6Rel))
print()

notAoiRel = rel_saccade_angle(notAoiCoords)
print("NOT_AOI Relative Saccade Angles: " + str(notAoiRel))
print()
