from saccades import *

def saccade_length(coords):
    """
    Get the saccade length

    # Arguments
    cur_coords  -> [x, y] coordinates of the current point
    prev_coords -. [x, y] coordinates of the previous point
    """
    saccadeLengthList = []

    if len(coords) >= 2:
        for i in range(1, len(coords)):
            saccadeLengthList.append(calc_saccade_length(coords[i], coords[i-1]))


    return saccadeLengthList

def abs_saccade_angle(coords, useDegrees=True):
    """
    Calculate the absolute angle of 2 fixations using atan2
    # ARGUMENTS
    cur_coords  -> Current coordinates in [x, y] form
    prev_coords -> Previous coordinates in [x, y] form
    use_degrees -> True to return in degrees, False to return in radians
    """
    absSaccadeAngleList = []

    if len(coords) >= 2:
        for i in range(1, len(coords)):
            absSaccadeAngleList.append(calc_abs_angle(coords[i], coords[i-1], useDegrees))


    return absSaccadeAngleList

def rel_saccade_angle(coords, useDegrees=True):
    relSaccadeAngleList = []

    if len(coords) >= 3:
        for i in range(2, len(coords)):
            relSaccadeAngleList.append(calc_rel_angle(coords[i-1], coords[i-2], coords[i], useDegrees))

    return relSaccadeAngleList
