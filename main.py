from database import Database
from seed_data import *

db = Database('getting_started')
db.createTable('weather')
db.addColumn('weather', 'city')
db.addColumn('weather', 'year', 'int')
db.addColumn('weather', 'warm_month')
db.addColumn('weather', 'cold_month')
db.addColumn('weather', 'average_high', 'int')

# values = ['New York City', 2013, 'July', 'January', 62]
# db.insert('weather', values)
db.insertMany('weather', WEATHER)

db.createTable('cities')
db.addColumn('cities', 'name')
db.addColumn('cities', 'state')
db.insertMany('cities', CITIES)

dataFrame= db.getDataFrame("SELECT * FROM weather INNER JOIN cities ON city = name WHERE warm_month = 'July';")

string  = "The cities that are warmest in July are:"
for index, row in dataFrame.iterrows():
    string += ", " + row['city'] 

print string
db.close()
