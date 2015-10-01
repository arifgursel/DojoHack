""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Projectname(Model):
    def __init__(self):
        super(Projectname, self).__init__()

    def index(self):
        #This funtion returns all date from the corresponding table in the DB
        query = ""
        return self.db.query_db(query)

    def create(self, create_info):
        query = ""
        self.db.query_db(query)
        return True

    def update(self, content, id):
        query = ""
        self.db.query_db(query)
        return True

    def delete(self, id):
        query = ""
        self.db.query_db(query) 
        return True

    def checkData(self, data_info): #Many-2-Many Data Insertion/Update checks
        checkQuery = ""
        data = self.db.query_db(checkQuery)
        if data:
            pass    #replace this with what you want to do
        else:       #data doesnt exist and we cant create it
            #you can insert the data without error
            insertQuery = ""
            self.db.query_db(query) 
        return True

