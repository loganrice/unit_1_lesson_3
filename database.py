import sqlite3
import pandas as pd
from table import Table

class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def addColumn(self, table, column, dataType='text'):
        params = {'tableName': table, 'name': column, 'dataType': dataType}
        table = Table(params['tableName'], self.connection)
        table.update(params)

    def createTable(self, name):
        table = Table(name, self.connection)
        table.create() 

    def insert(self, table, values):
        table = Table(table, self.connection)
        table.insert(values)

    def insertMany(self, table, values):
        table = Table(table, self.connection)
        table.insertMany(values)
    
    def getDataFrame(self, sql):
        query = self.__runQuery(sql)
        cols = [desc[0] for desc in self.cursor.description]
        return pd.DataFrame(query, columns=cols)

    def __runQuery(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


