from django.db import models
from django.conf import settings
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name
    
class Grade(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name='grades')
    score = models.IntegerField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.student.name} - {self.course} : {self.score}"