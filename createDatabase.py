import sqlite3
import os

# Check if there is a db file already exists
if os.path.exists("assignment2.db"):
    print("Remove assignment2.db before creating a new one!")
    quit()

# Create the DB file
connection = sqlite3.connect('assignment2.db')

# Enable foreign keys
connection.execute('PRAGMA foreign_keys = 1')

# Create tables
connection.execute('''CREATE TABLE CITY
                      (cityCode INT PRIMARY KEY,
                       cityName TEXT NOT NULL
                      );''')
connection.execute('''CREATE TABLE ROLES
                      (roleID INT PRIMARY KEY,
                       roleName TEXT NOT NULL
                      );''')
connection.execute('''CREATE TABLE STAFF
                      (staffID INT PRIMARY KEY,
                       username TEXT NOT NULL UNIQUE,
                       password TEXT NOT NULL,
                       roleID INT NOT NULL,
                       FOREIGN KEY (roleID) REFERENCES ROLES(roleID) ON UPDATE CASCADE
                      );''')
connection.execute('''CREATE TABLE HISTORICAL_PLACE
                      (hpCode INT PRIMARY KEY,
                       hpName TEXT NOT NULL,
                       hpCityCode INT NOT NULL,
                       hpManagerID INT NOT NULL UNIQUE,
                       FOREIGN KEY(hpCityCode) REFERENCES CITY(cityCode)
                       FOREIGN KEY(hpManagerID) REFERENCES STAFF(staffID)
                      );''')
connection.execute('''CREATE TABLE VISITOR
                       (date DATE,
                       numOfTourists INT NOT NULL,
                       numOfLocalVisitors INT NOT NULL,
                       numOfMaleVisitors INT NOT NULL,
                       numOfFemaleVisitors INT NOT NULL,
                       hpCode INT,
                       PRIMARY KEY (date, hpCode),
                       FOREIGN KEY (hpCode) REFERENCES HISTORICAL_PLACE(hpCode) ON UPDATE CASCADE
                      );''')

# Insert the values to tables
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (1, 'Gazimagusa');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (2, 'Girne');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (3, 'Guzelyurt');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (4, 'Iskele');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (5, 'Lefke');''')
connection.execute('''INSERT INTO CITY (cityCode,cityName) VALUES (6, 'Lefkosa');''')

connection.execute('''INSERT INTO ROLES (roleID,roleName) VALUES (1, 'Administrator');''')
connection.execute('''INSERT INTO ROLES (roleID,roleName) VALUES (2, 'Historical Place Manager');''')

connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (1, '1001HPM', '1234', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (2, '1002HPM', '5678', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (3, '1003HPM', '9123', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (4, '1004HPM', '4567', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (5, '1005HPM', '8912', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (6, '1006HPM', '3456', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (7, '1007HPM', '7891', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (8, '1008HPM', '2345', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (9, '1009HPM', '6789', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (10, '1010HPM', '1234', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (11, '1011HPM', '5678', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (12, '1012HPM', '9123', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (13, '1013A', '4567', 1);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (14, '1014A', '8912', 1);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (15, '1015A', '3456', 1);''')

connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (1, 'Othello Castle', 1, 1);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (2, 'St. Barnabas Monastery', 1, 2);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (3, 'St. Hilarion Castle', 2, 3);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (4, 'Bellapais Abbey', 2, 4);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (5, 'Guzelyurt Museum', 3, 5);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (6, 'St. Mamas Monastery', 3, 6);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (7, 'Apostolos Andreas Monastery', 4, 7);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (8, 'Kantara Castle', 4, 8);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (9, 'Soli', 5, 9);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (10, 'Vouni Palace', 5, 10);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (11, 'St. Sophia Cathedral', 6, 11);''')
connection.execute('''INSERT INTO HISTORICAL_PLACE (hpCode,hpName,hpCityCode,hpManagerID) VALUES (12, 'Dervis Pasa Mansion', 6, 12);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-01-01", 5,6,6,5,3);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-01-11", 10,20,9,11,4);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-01-10", 2,30,1,32,5);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-01-09", 10,50,20,30,9);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-02-06", 3,7,1,10,1);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-03-01", 4,6,2,9,2);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-01", 5,5,3,7,3);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-04-01", 6,4,4,6,4);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-05", 7,3,5,5,5);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-04", 52,1,1,52,6);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-03", 90,80,160,10,7);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-01", 5,6,1,10,8);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-08", 5,60,45,20,9);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-06", 15,6,20,1,10);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-12", 5,6,1,10,11);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-11", 5,6,1,10,12);''')
connection.execute('''INSERT INTO VISITOR (date, numOfTourists, numOfLocalVisitors, numOfMaleVisitors, numOfFemaleVisitors, hpCode) VALUES ("2020-05-10", 5,6,1,10,12);''')
connection.commit()
connection.close()