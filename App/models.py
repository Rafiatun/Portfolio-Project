from django.db import models

# Create your models here.

class Skill(models.Model):
    icon=models.ImageField(upload_to="media")

class Projects(models.Model):
    project_name=models.CharField(max_length=150,null=True,blank=True)
    tools=models.CharField(max_length=150,null=True,blank=True)
    project_link=models.URLField(null=True,blank=True)
    project_img=models.ImageField(upload_to="media")