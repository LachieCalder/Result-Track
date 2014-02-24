from django.shortcuts import render
from django.http import HttpResponseRedirect
from results.models import Assignment, Result, Student

def about(request):
    return render(request, 'static/about.html', {'title': 'About'})

def home(request):
    if request.user_is_authenticated():

        # get the student object associated with the logged in user
        current_student = Student.objects.filter(user = request.user)

        # get all assignments associated with this student
        assignments = Result.objects.filter(student = current_student)

        return render(request, 'home.html', {'assignments': assignments})
    else:
        return HttpResponseRedirect("../login")