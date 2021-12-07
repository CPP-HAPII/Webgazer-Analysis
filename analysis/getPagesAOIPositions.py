import mysql.connector
import pandas as pd

filePageCounter = 1

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
    sql_select_query_userAOI = "select * from UserAOIPositions where userID=2793"
    cursor = connection.cursor()
    cursor.execute(sql_select_query_userAOI)
    # get all records for user
    aoiRecords = cursor.fetchall()
    print("Total number of rows for aoi data: ", cursor.rowcount)

    print("\nPrinting page aoi positions into csv files")
    for data in aoiRecords:
        aoiData = [
            data[3], data[4], data[5], data[6],
            data[7], data[8], data[9], data[10],
            data[11], data[12], data[13], data[14],
            data[15], data[16]
        ]

        # writing to csv
        csvColumns = [
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
        page = pd.DataFrame([aoiData], columns=csvColumns)
        page.to_csv('user5/user5AOIPages/aoipage{}.csv'.format(filePageCounter), index=False)
        filePageCounter += 1


except KeyError as e:
    print("Error while connecting to MySQL db", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
