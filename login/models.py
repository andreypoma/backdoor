from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #letters_validator = re.compile(r'^[a-zA-Z]$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address."
        #check that email is unique
        emails = []
        for user in User.objects.all():
            emails.append(user.email)
        if postData['email'] in emails:
            errors['email'] = "This email was used already, please try another one."
        if postData['password'] != postData['pw_conf']:
            errors['password'] = "Passwords do not match"
        if len(postData['password']) < 3:
            errors['password'] = "Passwords should be at least 3 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
