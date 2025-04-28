from django.db import models

# Create your models here.
class User(models.Model):
    student_name = models.CharField(max_length=100, default='')
    teacher_name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.email)

