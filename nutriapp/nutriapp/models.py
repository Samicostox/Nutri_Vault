
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings





   

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique= True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    isemailvalid = models.BooleanField(default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Meal(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    complexity = models.IntegerField() # 0 easy , 1 medium, 2 hard
    description = models.CharField(max_length=255) # description of the meal
    ingredients = models.CharField(max_length=255) # implement that as an array field later
    time = models.IntegerField()
    steps = models.CharField(max_length=255) # description of the recipes (steps ect)
    nutri_values = models.CharField(max_length=255) # calories , fat, sugar etc



class Preferences(models.Model):
    fav_ingredients = models.CharField(max_length=255) # implement that as an array field later
    fav_crountry_meal = models.CharField(max_length=255)
    budget = models.IntegerField()
    fav_complexity = models.IntegerField() # 0 easy , 1 medium, 2 hard
    fav_meals = models.CharField(max_length=255) # implement that as an array field later
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    #One to One relation to User
    
class Physic(models.Model):
    height = models.IntegerField()
    weight = models.IntegerField() # make it a list to see progression in charts
    goal = models.CharField(max_length=255) # losing weight , gaining weight ect
    duration = models.CharField(max_length=255) # change to date time field later
    user = models.ForeignKey(User,on_delete=models.CASCADE)


