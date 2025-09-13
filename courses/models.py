from django.db import models
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    students = models.ManyToManyField("students.Student", related_name='courses')
    
    
    def __str__(self):
        return self.name
