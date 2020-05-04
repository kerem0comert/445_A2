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
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (10, '10010HPM', '1234', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (11, '10011HPM', '5678', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (12, '10012HPM', '9123', 2);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (13, '10013A', '4567', 1);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (14, '10014A', '8912', 1);''')
connection.execute('''INSERT INTO STAFF (staffID,username,password,roleID) VALUES (15, '10015A', '3456', 1);''')

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

connection.commit()
connection.close()