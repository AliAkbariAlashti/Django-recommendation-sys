from django.db import models

# Create your models here.
class user (models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    
    
class movies (models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    imdb_score = models.IntegerField()
    
    
class UserInterests(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    interested_geners = models.CharField(max_length=255)
    interested_director = models.CharField(max_length=255)
    favorite_movies = models.JSONField(default=list)
     