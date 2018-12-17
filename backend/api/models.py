from django.db import models

# Create your models here.


class Class(models.Model):
    code = models.CharField(max_length=5)
    class_name = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    length = models.CharField(max_length=25)
    weighted = models.BooleanField()
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    qualification = models.CharField(max_length=250)
    career = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=5000, blank=True)
    prerequisite = models.CharField(max_length=250, blank=True)
    link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.class_name
