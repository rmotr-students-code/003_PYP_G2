"""
import pyp_database
from datetime import date

pyp_database.create_database('imdb')
db = pyp_database.use('imdb')

db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8)) # Note 1
db.actors.query(name='Kevin Bacon') # Note 2

db.actors.query(name__like='Kevin%')
db.actors.query(name__ilike='%bacon%') # ilike means case insensitive
db.actors.query(date_of_birth__gt=date(1950, 1, 1)) # gt means "greater than"
db.actors.query(date_of_birth__gte=date(1958, 7, 8)) # gte means "greater than or or equals to"

Steps

CREATION/SETUP

[ x ] 1. create empty database file based on name
[   ] 2. create table file  (tablename:filename?) or just use filename
[   ]    a.  add table file to database list
[   ]    b.  add default columns to table file
[   ] 3. add record to table 
[   ]    b.  validate records against column types

QUERY/UPDATE:

[   ] 4. implement use() select which database to limit tables
[   ] 5. query based on a column name  (slow scan)
        b.  validate column name
[   ] 6. update based on a column name (slow scan)

"""

import shelve

class Database(object):
    
    #self.dbname = None

    def create_database(self,name):
        myfilename = str(name)+".txt" #need to sanitize
        f = open(myfilename,"w") 
        f.close()
    
    def use(self,dbname):  # select which database to open
        self.dbname = dbname
    
    
    """
    d = {  '0' : { 'colname':'coltype', 'colname2':'coltype2' }.
           '1' : { 'id':1, 'name':'Neil' },
           '2' : { 'id':2, 'name':'Bob' },
           'Name_index' : {blah}
        }
    """

    def create_table(self, table_name, **cols):
        if self.dbname == None:
            raise "DB must be selected before creating a table"
        table_filename = str(self.dbname)+"_"+str(table_name) #need to sanitize
        d = shelve.open(table_name)
        for column_name,column_type in cols:
            d[0][column_name] = column_name
            d[0][column_type] = column_type
        d = shelve.close()
        # add table to database file
        
    
#cols: {'id':None, 'name':None'...}
#newvalues : {1,'Neil'}
#for key in range(len(cols)
#    cols[key] = newvalues[key]
    

class Table(object):
        
    def insert(self, *args):
        d = shelve.open(filename)
        cols = d[cols] # this gets the column names as keys
        for col in cols: # insert each new value for each column name
            pass

    #db.actors.query(name='Kevin Bacon') # Note 2                
    def query(self, key):
        pass   
    
    def delete(self,key):
        pass

db = Database()
db.create_database("imdb")
db.create_table('actors', columns={
    'id': int,
    'name': str,
    'date_of_birth': date,
    'nationality': {
        'type': str,
        'allow_none': True,
    }
})

    
#db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8))


