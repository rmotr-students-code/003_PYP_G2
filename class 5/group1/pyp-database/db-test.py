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

"""

import pyp_database
from datetime import date

pyp_database.create_database('imdb')

