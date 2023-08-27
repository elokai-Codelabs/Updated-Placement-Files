from django.db import models
from .utils import *

# Create your models here.


class Course(models.Model):
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"
    
class Program(models.Model):
    name = models.CharField(max_length=400)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Grade(models.Model):
    name = models.CharField(max_length=400, choices=AVAILABLE_GRADES)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name