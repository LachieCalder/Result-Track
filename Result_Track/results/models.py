from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):

    # one to one relationship with a user authentication object
    user = models.OneToOneField(User)
    year_level = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()

class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher')

class Teacher(models.Model):
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Result(models.Model):
    student = models.ForeignKey('Student')
    assignment = models.ForeignKey('Assignment')
    mark = models.PositiveSmallIntegerField()
    marked = models.BooleanField(default=False)

class Assignment(models.Model):
    due_date = models.DateField()
    possible_mark = models.PositiveSmallIntegerField()
    course = models.ForeignKey('Course')
    name = models.CharField(max_length=50)
    details = models.TextField()
