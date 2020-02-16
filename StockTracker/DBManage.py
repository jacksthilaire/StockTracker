import sqlite3

# methods: create database, add to database, delete from database, retrieve all data and input into list
dbcon = sqlite3.connect('StockDB.db')


def createDB():
    try:
        dbcon.execute("CREATE TABLE Stocks(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name TEXT NOT NULL);")
        dbcon.commit()
    except sqlite3.OperationalError:
        print("Operational Error: Table already created?")


def addDB(name):
    dbcon.execute("INSERT INTO Stocks (Name) VALUES ('{}')".format(name))
    dbcon.commit()


def delDB(name):
    dbcon.execute("DELETE FROM Stocks WHERE Name='{}'".format(name))
    dbcon.commit()


def retrieveDB():
    try:
        stocklist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        theCursor = dbcon.cursor()
        cursor_results = theCursor.execute("SELECT * FROM Stocks")

        # for every row add the name to a list
        i = 0
        for row in cursor_results:
            stocklist[i] = row[1]
            i += 1
        return stocklist
    except sqlite3.OperationalError:
        print("Operational Error")

