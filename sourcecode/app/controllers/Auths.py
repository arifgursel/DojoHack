"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Auths(Controller):
    def __init__(self, action):
        super(Auths, self).__init__(action)
        self.load_model('Auth') 

    def index(self):
        return self.load_view('index.html')

    def reset(self):
        session.clear()
        return redirect('/')

    def process_reg(self):
        reg_info = {'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'email': request.form['email'],
                    'password1': request.form['password1'],
                    'password2': request.form['password2']
                    }
        print 'Heres what we got from the form:', reg_info
        reg_status = self.models['Auth'].process_reg(reg_info)
        if reg_status['status'] == True:
            session['id'] = reg_status['user']['id'] 
            session['first_name'] = reg_status['user']['first_name']
            session['last_name'] = reg_status['user']['last_name']
            session['full_name'] = session['first_name'] + ' ' + session['last_name']
            return redirect('/postauth')
        else:
            for error in reg_status['errors']:
                flash(error)
            return redirect('/')
            
    def process_log(self):
        login_info = {'email': request.form['email'],
                    'password': request.form['password']
                    }
        login_status = self.models['Auth'].process_log(login_info)
        if login_status['status'] == True:
            session['id'] = login_status['user']['id'] 
            session['first_name'] = login_status['user']['first_name']
            session['last_name'] = login_status['user']['last_name']
            session['full_name'] = session['first_name'] + ' ' + session['last_name']
            return redirect('/postauth')
        else:
            for error in login_status['errors']:
                flash(error)
            return redirect('/')

