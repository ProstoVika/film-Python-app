import sqlite3 as sql

try:
  with sql.connect('project film/filmflix.db') as db_con:
       db_cursor = db_con.cursor()
except sql.OperationalError as oe: 
    print(f'Connection failed because: {oe}')
