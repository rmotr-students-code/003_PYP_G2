import unittest, os, pyp_database, shelve
from datetime import date

class tests(unittest.TestCase):
    
    def test_db(self):
        
        pyp_database.create_database('imdb') 
        self.assertTrue(os.path.isfile('imdb_db.dat'))
    
    def test_tables(self):
        db = pyp_database.use('imdb')
        self.assertIsInstance(db, pyp_database.Database)
        db.create_table('actors', columns=['id', 'name', 'date_of_birth'])
        self.assertTrue(os.path.isfile('imdb_actors.dat'))
        
        #self.assertEqual(d['headers'],{'id':None,'name':None,'date_of_birth':None})
        db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8))
        d = shelve.open('imdb_actors.dat')
        for key,value in d.items():
            if key != 'headers':
                self.assertEqual(value,1,'Kevin Bacon', date(1958, 7, 8))
        
    ''' def tearDown(self):
        os.remove('imdb_db.dat')
        os.remove('imdb_actors.dat')'''
        
if __name__ == '__main__':
    unittest.main()