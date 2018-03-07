import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_password):
        errorlist = []
        the_user = User.objects.filter(email = email)
        if len(first_name) < 2:
            errorlist.append("First name is too short")            
        if len(last_name) < 2:
            errorlist.append("Last name is too short")           
        if not EMAIL_REGEX.match(email):
            errorlist.append('Please enter a valid email') 
        if the_user:
            errorlist.append("Email already taken")           
        if confirm_password != password:
            errorlist.append("Passwords don\'t match")
        if len(password) < 8:
            errorlist.append("Please enter a password longer than 8 characters")
        if len(errorlist) > 0:
            return errorlist
        else:
            return True

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()