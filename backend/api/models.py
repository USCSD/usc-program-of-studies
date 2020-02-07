from django.db import models

# Create your models here.


class Class(models.Model):
    code = models.CharField(max_length=10)
    class_name = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    length = models.CharField(max_length=25)
    weighted = models.BooleanField()
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    qualification = models.TextField(max_length=250, blank = True)
    careers = models.ManyToManyField('Career',blank=True)
    description = models.TextField(max_length=5000, blank=True)
    prerequisite = models.TextField(max_length=250, blank=True)
    link = models.CharField(max_length=100, blank=True)
    mods = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.class_name

class Career(models.Model):
    career_name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, blank=True)
    career_pathways = models.TextField(max_length=5000,blank=True)
    suggested_classes = models.ManyToManyField(Class,blank=True)

    def __str__(self):
        return self.career_name

class Info(models.Model):
    info_name = models.CharField(max_length=100)
    file_name = models.FileField()

    def __str__(self):
        return self.info_name
