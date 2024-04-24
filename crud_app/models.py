from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=250)
    project_repo = models.CharField(max_length=100)
