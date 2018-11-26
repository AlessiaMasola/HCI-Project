from django.db import models


class User (models.Model):
    # Add a check to ensure max_length isn't exceeded? (for all classes)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)  
    email    = models.EmailField()
    picture = models.CharField(max_length=255, default='')

    def __unicode__(self):
        return self.username

    # def __str__(self):
    #     return self.username

    # def __unicode__(self):
    #     return self.first_name

class Event (models.Model):
    name        = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    # start_date_time = models.DateTimeField()
    # end_date_time   = models.DateTimeField()

    def __unicode__(self):
        return self.name