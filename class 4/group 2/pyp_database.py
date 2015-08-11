'''
A module for creating databases which are stored in plaintext files under the hood.
Use like a regular database.
'''

'''
You'll need to build a simple database system using files. That your database is using files underneath should be COMPLETELY hidden to your user. This is the database interface that we need:

import pyp_database
from datetime import date

pyp_database.create_database('imdb')
db = pyp_database.use('imdb')

db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8)) # Note 1
db.actors.query(name='Kevin Bacon') # Note 2
This database should be carefully packaged so it can be imported by some other program. WE DON'T WANT SCATTERED SCRIPTS ANYMORE. Improve your coding: more readable, documented, tested, self-packaged.

Note 1: Pay attention to the interface. We're doing db.actors, which is the name of the table. You'll have to work with dynamic attributes (__getattr__) or properties in order to solve that. Also, be careful on the type of data you're receiving. You should format dates, strings and numbers without issues.

Note 2: The attribute passed to query will also be dynamic and it'll depend on the columns present in the table.

All these are improvements you can do:

Better queries

An improvement would be to provide a richer interface for queries. For example:

db.actors.query(name__like='Kevin%')
db.actors.query(name__ilike='%bacon%') # ilike means case insensitive
db.actors.query(date_of_birth__gt=date(1950, 1, 1)) # gt means "greater than"
db.actors.query(date_of_birth__gte=date(1958, 7, 8)) # gte means "greater than or or equals to"
Indexes and unique values

Allow index creation on tables. Indexes might be also be used to check for unique values.

db.actors.index('name')  # Created an index in the name column
db.actors.index('id', unique=True)  # Created an index in the id column and it MUST be a unique value across the whole table.
Data validation and default values

Create tables indicating the data type for each column and if the value can be None or not:

db.create_table('actors', columns={
    'id': int,
    'name': str,
    'date_of_birth': date,
    'nationality': {
        'type': str,
        'allow_none': True,
    }
})

db.actors.insert('2', 'Julia Roberts', date(1958, 7, 8)) # This should fail because id is not an int
db.actors.insert(2, 'Julia Roberts', '1967') # This should fail because date is invalid
db.actors.insert(2, 'Julia Roberts', date(1967, 10,28)) # This succeeds and sets nationality to None
CLI interface

It'd be really nice to have a Command Line Interface program to interact with databases:

$ python pyp_database create_database imdb
$ python pyp_database -d imdb create_table actors id,name,date_of_birth
$ python pyp_database -d imdb -t actors insert --id 1 --name "Kevin Bacon" --date_of_birth "1958-07-08"
$ python pyp_database -d imdb -t actors query --name "Kevin Bacon"
$ python pyp_database -d imdb -t actors query --name__like "Kevin%"
Installable Package

Using setuptools publish your package to the cheeseshop (pypi.python.org) and make it installable to anyone. So I should be able to do:

$ pip install pyp_database
and use your database in my own project.
'''

'''
d = { 
'headers' : { 'name':'Neil', 'address':'blah'},
'1' : { 'name':'Neil', 'address':'blah' }, 
'2' : { 'name':'Neil2', 'address':'blah2'}, 
'3' : { 'name':'Neil3', 'address':'blah3'} 
},

but to find db.actors.query(name="Neil"), you have to scan through 
all rows since there is no "name" key.

for k, v in d:
    if d[k]['name'] == name:
    if d[k]['add'] == address:
    if 




if name:
    d = d_name

for each in d_name:
    if d[each] == 'name'
    
[name, add, id, blach blah] # to return to user

res = []
res.append(id)

for each in [of dictionaries]
    for k in each:
        if k == id:
            res.append(
    
d_name = {'id1': 'name1',
     'id2': 'name2',
     'id3': 'name3',
     'id4': 'name4',
     'id5': 'name5',
     'id6': 'name6',
     }
d_address = { 'id1': 'add1',
              'id2': 'add2',
              'id3': 'add3',
              'id4': 'add4',
              'id5': 'add5',
              'id6': 'add6',
     }

db.tablename.query(name="whatever")


'''
import shelve,uuid,os
from datetime import date

def create_database(name):
    '''
    Creates a table. Pass in a name argument.
    '''
    dbfile = name + '_db.dat'
    with open(dbfile, 'a') as database:
        database.write('')
        
def use(name):
    '''
    Selects the active database. pass in a name arguement.
    '''
    #do checks to make sure name is in dbfile
    #select it or read from that file.
    return Database(name)
    
class Database(object):

    def __init__(self, name):
        self.db_name = name

    # db.actors.query(name="Neil")
    def __getattr__(self, tablename):
        return Table(self.db_name,tablename)
        
    def create_table(self, table_name, columns=[]):
        '''
        we need to know which db it belongs to  ( self.current_db )
        db_tablename  /db/tablename.txt
        '''
        dbfile = self.db_name + '_db.dat'
        
        # add to database table
        with open(dbfile, "a") as f:
            f.write(table_name)
        
        # create table file and write columns in first key
        table_file = self.db_name + "_" + table_name + '.dat'
        table_dict = shelve.open(table_file)
        table_dict['headers'] = columns
        table_dict.close()
        
class Table(object):
    
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.name = table_name
        self.table_file = self.db_name + '_' + self.name + '.dat'
    
    def insert(self, *cols):
        '''dbname_tablename.dat'''
    
        d = shelve.open(self.table_file)
        headers = d['headers']
        #['name', 'age', etc]
        # DOES preserve order
        tmp = {}
        for header, column in zip(headers, cols):
            print "header: {}, column: {}".format(header, column)
            if not isinstance(column, int):
                tmp[header] = str(column)
            else: tmp[header] = column
        myuuid = str(uuid.uuid1())
        d[myuuid] = tmp
        d.close()
    
    def query(self, **kwargs):
        # kwargs = {'name': 'Kevin Bacon'}
        # kwargs.keys() = ['name']
        # kwargs.values() = ['Kevin Bacon']
        col_name = kwargs.keys()[0]
        searched_value = kwargs.values()[0]
        print "searched value = {}".format(searched_value)
        d = shelve.open(self.table_file)
        found = {}
        for uuid, record_dictionary in d.items():
            if not isinstance(record_dictionary,list):
                #print "record_dictionary " + str(record_dictionary)
                if record_dictionary[col_name] == searched_value:
                    found = d[uuid]
        d.close()
        if found:
            return found
        else:
            print "No Records Found"
        
    
    def show_table(self,name):
       d = shelve.open(name)
       print d
       
        
def tearDown():
    os.remove('imdb_db.dat')
    os.remove('imdb_actors.dat')

db = use('imdb')
db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8))
#db.actors.show_table("imdb_actors.dat")
print "query result:"
print db.actors.query(name='Kevin Bacon') 
print db.actors.query(name='Julia Roberts')
print db.actors.query(date_of_birth='1958-07-08')
tearDown()