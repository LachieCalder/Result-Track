from django.db import models
from django.contrib.auth.models import User
import datetime

class Student(models.Model):

    # one to one relationship with a user authentication object
    user = models.OneToOneField(User)
    year_level = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name + ' ' + self.surname

class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher')

    def __unicode__(self):
        return self.name

class Teacher(models.Model):
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name + ' ' + self.surname

class Result(models.Model):
    student = models.ForeignKey('Student')
    assignment = models.ForeignKey('Assignment')
    mark = models.PositiveSmallIntegerField()
    marked = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.student) + "'s " + str(self.assignment)

    def is_overdue(self):
        base_assignment = Assignment.objects.get(pk=self.assignment)
        if base_assignment.due_date >= datetime.date.today():
            return True
        else:
            return False

class Assignment(models.Model):
    due_date = models.DateField()
    possible_mark = models.PositiveSmallIntegerField()
    course = models.ForeignKey('Course')
    name = models.CharField(max_length=50)
    details = models.TextField()

    def __unicode__(self):
        return self.name
