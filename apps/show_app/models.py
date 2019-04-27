from __future__ import unicode_literals
from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["s_tit"]) < 2:
            errors["s_tit"] = "Title name should be at least 2 characters"
        if len(postData['s_net']) < 2:
            errors["s_net"] = "Network name should be at least 2 characters"
        if len(postData['s_des']) < 5:
            errors["s_des"] = "Description should be at least 5 characters"
        # if len(postData['s_rel']) < 2:
        #     errors["s_rel"] = "Release data should be at least 2 characters"
        
        # edit  validation
        # if len(postData["e_tit"]) < 2:
        #      errors["e_tit"] = "Title name should be at least 2 characters"
        # if len(postData['e_net']) < 2:
        #      errors["e_net"] = "Network name should be at least 2 characters"
        # if len(postData['e_rel']) < 2:
        #      errors["e_rel"] = "Release data should be at least 2 characters"
        # if len(postData['e_des']) < 5:
        #      errors["e_des"] = "Description should be at least 5 characters"
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 

