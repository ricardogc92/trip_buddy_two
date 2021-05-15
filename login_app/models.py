from enum import unique
from django.db import models
import re


# Create your models here.
class UsersManager(models.Manager):
    def validator(self, post_data):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name'])<2:
            errors['first_name']="First Name muust be at least 2 characters."
        if len(post_data['last_name'])<2:
            errors['last_name']="Last Name must be at least 2 characters."
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']="Email address is not valid."
        if len(post_data['password'])<8:
            errors['password']="Password must be at least 8 characters."
        if post_data['password'] != post_data['confirm']:
            errors['confirm']="Confirm Password is not matching."
        check = User.objects.filter(email=post_data['email'])
        if len(check) > 0:
            errors['repeat']="Email already exists"
        return errors


class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UsersManager()