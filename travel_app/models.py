from django.db import models
from login_app.models import User
from datetime import date

# Create your models here.


class TripManager(models.Manager):
    def validator(self, post_data):
        errors={}
        today=str(date.today())
        print(today)
        print(post_data['start_date'])
        if len(post_data['destination'])<3:
            errors['destination']="Destination must be at least 3 characters."
        if len(post_data['plan'])<3:
            errors['plan']="Plan must be at least 3 characters."
        if not post_data['start_date']:
            errors['empty_start']="Start date can't be empty."
        if not post_data['end_date']:
            errors['empty_end']="End date can't be empty."
        if post_data['start_date'] and post_data['start_date']<today:
            errors['start_date']="Start date can't be in the past"
        if post_data['start_date']>post_data['end_date']:
            errors['end_date']="End date must be after start date."
        return errors


class Trips(models.Model):
    destination=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    plan=models.CharField(max_length=255)
    owner=models.ForeignKey(User, related_name="trips_created", on_delete=models.CASCADE)
    users_joined=models.ManyToManyField(User, related_name="trips_joined")
    objects=TripManager()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)


