from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length = 255, db_index = True, null = True, blank = True)
    age = models.IntegerField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
