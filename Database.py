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

    def createReport(self, queryDetails):
        selection = int(queryDetails[0])
        if (selection == 1):
            dbCursor = self.db.cursor()
            dbCursor.execute("SELECT h.hpName FROM HISTORICAL_PLACE h, (SELECT MAX(numOfFemaleVisitors+numOfMaleVisitors) AS MaximumVisitors, hpCode FROM VISITOR) v WHERE h.hpCode=v.hpCode")
            queryResult = dbCursor.fetchall()
            dbCursor.close()
            try:
                queryTuple = queryResult[0]
                return queryTuple[0]
            except: return "None"
        elif (selection == 2):
            dbCursor = self.db.cursor()
            dbCursor.execute('''SELECT cityName, MAX(sumFemale+sumMale) FROM 
                               (SELECT cityName, sum(numOfFemaleVisitors) as sumFemale, sum(numOfMaleVisitors) as sumMale FROM 
                               HISTORICAL_PLACE h, CITY c, VISITOR v WHERE h.hpCode=v.hpCode and c.cityCode=h.hpCityCode GROUP BY cityName)''')
            queryResult = dbCursor.fetchall()
            dbCursor.close()
            try:
                queryTuple = queryResult[0]
                return queryTuple[0]
            except: return "None"
        elif (selection == 3):
            dbCursor = self.db.cursor()
            dbCursor.execute('''SELECT cityName, SUM(numOfMaleVisitors), sum(numOfFemaleVisitors), sum(numOfLocalVisitors), sum(numOfTourists) FROM 
                                HISTORICAL_PLACE h, CITY c, VISITOR v WHERE h.hpCode=v.hpCode and c.cityCode=h.hpCityCode GROUP BY cityName''')
            queryResult = dbCursor.fetchall()
            dbCursor.close()
            return queryResult
        elif (selection == 4):
            hpCityCode = int(queryDetails[1])
            dbCursor = self.db.cursor()
            dbCursor.execute('''SELECT cityName, SUM(numOfMaleVisitors), sum(numOfFemaleVisitors), sum(numOfLocalVisitors), sum(numOfTourists) FROM 
                                HISTORICAL_PLACE h, CITY c, VISITOR v WHERE h.hpCode=v.hpCode and c.cityCode=h.hpCityCode and h.hpCityCode=? GROUP BY 
                                cityName''', (hpCityCode,))
            queryResult = dbCursor.fetchall()
            dbCursor.close()
            try:
                return queryResult[0]
            except: return ("None", 0, 0, 0, 0)
        elif (selection == 5):
            hpCode = int(queryDetails[1])
            date = queryDetails[2]
            dbCursor = self.db.cursor()
            dbCursor.execute("SELECT numOfMaleVisitors, numOfFemaleVisitors, numOfLocalVisitors, numOfTourists FROM HISTORICAL_PLACE h, VISITOR v WHERE h.hpCode=v.hpCode and h.hpCode={} and v.date={}".format(hpCode, date))
            queryResult = dbCursor.fetchall()
            dbCursor.close()
            try:
                return queryResult[0]
            except: return (0, 0, 0, 0)
        


