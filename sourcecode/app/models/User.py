""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def index(self):
        #access some data
        query = "SELECT * FROM users"
        return self.db.query_db(query)

    
