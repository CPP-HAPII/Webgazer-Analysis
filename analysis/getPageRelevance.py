import mysql.connector
import pandas as pd

filePageCounter, pageCounter = 1, 1
relevanceData = []

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
    sql_select_query_user = "select * from Relevance where userID=2793"
    cursor = connection.cursor()
    cursor.execute(sql_select_query_user)
    # get all records for user
    relRecords = cursor.fetchall()
    print("Total number of rows for user eye gaze data: ", cursor.rowcount)

    print("\nPrinting relevance data into csv files")
    for data in relRecords:
        if data[3] == 5:
            tempList = [
                pageCounter,
                data[2],
                data[3],
                data[4],
                data[5]
            ]
            relevanceData.append(tempList)
            pageCounter += 1
        else:
            tempList = [
                pageCounter,
                data[2],
                data[3],
                data[4],
                data[5]
            ]
            relevanceData.append(tempList)

    # writing to csv
    page = pd.DataFrame(relevanceData, columns=['Page', 'Result ID', 'Result Number', 'Relevance', 'Query Language'])
    page.to_csv('user5/user5RelevanceData/user5Relevance.csv', index=False)


except KeyError as e:
    print("Error while connecting to MySQL db", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
