import pandas as pd

def getAllPageFixations(input_file):
    col_list1 = [
        'AOI1',
        'AOI2',
        'AOI3',
        'AOI4',
        'AOI5',
        'AOI6',
        'NOT_AOI'
    ]
    df1 = pd.read_csv(input_file, usecols=col_list1)

    allFixationsList = [df1.values[0][0], df1.values[0][1], df1.values[0][2], df1.values[0][3], df1.values[0][4], df1.values[0][5], df1.values[0][6]]

    return allFixationsList
