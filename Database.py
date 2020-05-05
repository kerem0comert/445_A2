import sqlite3
import os

dbFileName = "assignment2.db"

class Database():
    def __init__(self):
        self.db = sqlite3.connect(dbFileName, check_same_thread=False)

    def login(self, username, password):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT staffID,roleID FROM STAFF WHERE username = ? AND password = ?", (username,password,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple
        except: return (0,0)

    def getHpCode(self, HpManagerID):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT hpCode FROM HISTORICAL_PLACE WHERE hpManagerID = ?", (HpManagerID,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return 0

    def getHpName(self, HpCode):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT hpName FROM HISTORICAL_PLACE WHERE hpCode = ?", (HpCode,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return "None"

    def getHpCityName(self, HpCode):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT c.cityName FROM HISTORICAL_PLACE hp, CITY c WHERE hp.hpCode = ? AND hp.hpCityCode = c.cityCode", (HpCode,))
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        try:
            queryTuple = queryResult[0]
            return queryTuple[0]
        except: return "None"

    def getCities(self):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT cityCode,cityName FROM CITY")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def getHistoricalPlaces(self):
        dbCursor = self.db.cursor()
        dbCursor.execute("SELECT hpCityCode,hpCode,hpName FROM HISTORICAL_PLACE")
        queryResult = dbCursor.fetchall()
        dbCursor.close()
        return queryResult

    def sendStatistics(self, reportDetails):
        # reportDetails -> [totVisitors, maleVisitors, femaleVisitors, localVisitors, tourists, hpCode]
        try:
            self.db.execute('''INSERT INTO VISITOR (date,numOfTourists,numOfLocalVisitors,numOfMaleVisitors,numOfFemaleVisitors,hpCode) 
                            VALUES (CURRENT_DATE, ?, ?, ?, ?, ?);''', (reportDetails[4],reportDetails[3],reportDetails[1],reportDetails[2],reportDetails[5],))
            self.db.commit()
            return 0
        except: return 1 # statistics can be only 1 per day


