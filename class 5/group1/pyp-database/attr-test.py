class Database:
    
    def __init__(self,db_name):
        self.db_name = name
        
    def use(self,db_name):
        self.db_name = name
    
    def __getattr__(self, table_name): # if not a valid method, we have table name
        return Table(self.db_name,table_name)
        

class Table:
    
    def __init__(self,db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.db_file_name = str(db_name)+"_"+str(table_name)
        
    def __getattr__(self, method):
        print "sorry, that method does not exist"
        
    def query(self,*args):
        print "made it into query"
        print args
        
    def select(self):
        print "made it into select"
        
    def update(self):
        print "made it into update"


db = Database("imdb")  
db.actors.query("mike") #db is now actually a Table object!
