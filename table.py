class Table:
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection
        self.attributes = {} 

    def create(self):
        self.__hasTableBeenCreated
        sql = 'CREATE TABLE {} (ID INTEGER PRIMARY KEY)'.format(self.name)
        self.__commit(sql)

    def update(self, params={}):
        table = self.name
        column = params['name']
        dataType = params['dataType']

        sql = 'ALTER TABLE {} ADD COLUMN {} {}'.format(table, column, dataType)
        self.__commit(sql)

    def insert(self, values):
        sqlValues = self.__convertArrayToSQLValues(values)
        sql = "INSERT INTO {} VALUES({})".format(self.name, sqlValues)
        self.__commit(sql)

    def insertMany(self, values):
        for value in values:
            self.insert(value)

    def __hasTableBeenCreated(self):
        sql = 'DROP TABLE IF EXISTS {};'.format(self.name)
        self.connection.commit(sql)
        
    def __commit(self, sql):
        self.connection.execute(sql)
        self.connection.commit()

    def __convertArrayToSQLValues(self, array):
        sql_values = "NULL"
        for value in array:
            if isinstance(value, int) or isinstance(value, float):
                sql_values += ", " + str(value) 
            else:
                sql_values += ", \'" + str(value) + "\'" 

        return sql_values

