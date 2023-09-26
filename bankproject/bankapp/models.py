from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class district(models.Model):
    districtname=models.CharField(max_length=250)

class branch(models.Model):
    branchname=models.CharField(max_length=250)
