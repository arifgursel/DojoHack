"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Projectnames(Controller):
    def __init__(self, action):
        super(Projectnames, self).__init__(action)
        self.load_model('Projectname')
    
    def index(self):    
        self.models['Projectname'].index()
        return self.load_view('postauth/index.html')
    
    
    def update(self):
        #Get form data and assign to variables

        #Call model to process data by passign appropriate variables
        self.models['Projectname'].update()
        #return True to indicate completion
        return True
    
    def create(self):
        #Get form data and assign to variables

        #Call model to create data by passign appropriate variables
        self.models['Projectname'].create()
        #return True to indicate completion
        return True
    
    def delete(self):
        #Get form data and assign to variables

        #Call model to create data by passign appropriate variables
        self.models['Projectname'].delete()
        #return True to indicate completion
        return True
    
    #method below is how you call index to sub folders in restful manner
    def index_partial(self):
        self.models['Projectname'].index_partial()
        #Load view of partial and data to indicate completion
        return self.load_view('postauth/index.html')
