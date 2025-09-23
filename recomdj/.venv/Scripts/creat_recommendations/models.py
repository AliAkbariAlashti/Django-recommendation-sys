from django.db import models

# Create your models here.

class UserActions (models.Model):
    action_id = models.IntegerField()
    user_id = models.IntegerField()
    action_type = models.CharField(max_length=255)
    action_value = models.CharField(max_length=255)
    
    
class Recommendations(models.Model):
    user_id = models.IntegerField()
    Recommendations = models.JSONField(default=list)
    