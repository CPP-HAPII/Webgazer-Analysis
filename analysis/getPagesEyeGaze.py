import mysql.connector
import pandas as pd
import ast

filePageCounter = 1
eyeGazeData = []

# connecting to HAPII database
try:
    connection = mysql.connector.connect(host='aa13mnjbzyz2hfy.ciyfv2p6bkbk.us-west-1.rds.amazonaws.com',
                                        database='HAPII',
                                        user='root',
                                        password='CPPHapii')

    if connection.is_connected():
        print("Successfully connected to database!")
    print("\n")

    # getting data for user 1
    sql_select_query_user = "select * from UserGaze where userID=2793"
    cursor = connection.cursor()
    cursor.execute(sql_select_query_user)
    # get all records for user
    records = cursor.fetchall()
    print("Total number of rows for user eye gaze data: ", cursor.rowcount)

    print("\nPrinting page gaze data into csv files")
    for data in records:
        # converting eye gaze strings to list
        stringEyeGaze = data[3]
        eyeGazeData = ast.literal_eval(stringEyeGaze)
        # print(eyeGazeData)

        # writing to csv
        page = pd.DataFrame(eyeGazeData, columns=['Time', 'X Coordinate', 'Y Coordinate'])
        page.to_csv('user5/user5Pages/page{}.csv'.format(filePageCounter), index=False)
        filePageCounter += 1


except KeyError as e:
    print("Error while connecting to MySQL db", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
