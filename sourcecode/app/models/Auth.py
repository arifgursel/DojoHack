""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
class Auth(Model):
    def __init__(self):
        super(Auth, self).__init__()

    def process_reg(self, reg_info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # some basic validations
        if not reg_info['first_name']:
            errors.append('First Name cannot be blank')
        elif len(reg_info['first_name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not reg_info['last_name']:
            errors.append('Last Name cannot be blank')
        elif len(reg_info['last_name']) < 2:
            errors.append('Last Name must be at least 2 characters long')
        if not reg_info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(reg_info['email']):
            errors.append('Email format must be valid!')
        if not reg_info['password1']:
            errors.append('Password cannot be blank')
        elif len(reg_info['password1']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif reg_info['password1'] != reg_info['password2']:
            errors.append('Password and confirmation must match!')
        # check if there are any errors, if there are any return the array
        # otherwise return True
        if errors:
            return {"status": False, "errors": errors}
        else:
            #Bcrypt the password
            password = reg_info['password1']
            pw_hash = self.bcrypt.generate_password_hash(password)
            # code to insert reg info into DB goes here
            create_user_query = "INSERT INTO users (`first_name`, `last_name`, `email`, `pw_hash`, `created_at`, `updated_at`) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW());".format(reg_info['first_name'], reg_info['last_name'],reg_info['email'], pw_hash)
            self.db.query_db(create_user_query)
            # retrieve the last inserted user from above so you can return and save session info
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user_query)
            return {"status": True, "user": user[0]} #always returns a list so we retrieve the first and hopefully only element

    def process_log(self, login_info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # some basic validations
        if not login_info['email']:
            errors.append('Must enter an email address!')
        elif not EMAIL_REGEX.match(login_info['email']):
            errors.append('Email format must be valid!')
        if not login_info['password']:
            errors.append('Password cannot be blank')
        elif len(login_info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        # check if there are any errors, if there are any return the array
        # otherwise return True
        if errors:
            return {"status": False, "errors": errors}
        else:
            #check DB and retrieve record that matches that email address
            check_email_query = "SELECT * FROM users WHERE email = '{}';".format(login_info['email'])
            #always returns a list so we retrieve the first and hopefully only element
            user = self.db.query_db(check_email_query)
            #If in DB process the Bcrypt hash against supplied credentials
            if user:
                match = self.bcrypt.check_password_hash(user[0]['pw_hash'], login_info['password'])
                if match:
                    return {"status": True, "user": user[0]}
                else:
                    errors.append('Invalid password/email combination')
                    return {"status": False, "errors": errors}
            else:
                errors.append('No such user, please register!')
                return {"status": False, "errors": errors}
    
