# yourappname/models.py
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
