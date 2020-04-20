import sqlite3

connection = sqlite3.connect('assignment2.db')
connection.execute('''CREATE TABLE CITY
                      (cityCode INT PRIMARY KEY NOT NULL,
                       cityName TEXT NOT NULL
                      );''')
connection.execute('''CREATE TABLE HISTORICAL_PLACE
                      (hpCode INT PRIMARY KEY NOT NULL,
                       hpName TEXT NOT NULL
                      );''')
connection.execute('''CREATE TABLE STAFF
                      (staffID INT PRIMARY KEY NOT NULL,
                       username TEXT NOT NULL,
                       password TEXT NOT NULL
                      );''')                

"""It would be more appropriate to call this a 'visit' since it is not keeping track of 
any individual visitors but keeps track of a whole visit of many visitors with its numeric details"""

connection.execute('''CREATE TABLE VISIT
                      (date TIMESTAMP PRIMARY KEY NOT NULL,
                       localVisitors INT NOT NULL,
                       tourists INT NOT NULL,
                       males INT NOT NULL,
                       females INT NOT NULL
                      );''')

connection.commit()
connection.close()