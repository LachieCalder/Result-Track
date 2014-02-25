from django.shortcuts import render
from django.http import HttpResponseRedirect
from results.models import Result, Course
from results.utils import is_allowed

def about(request):
    return render(request, 'static/about.html', {'title': 'About'})

def home(request):
    if request.user.is_authenticated():

        # get the student object associated with the logged in user
        current_student = request.user.get_profile()

        results = Result.objects.filter(student=current_student, marked=True).order_by('assignment__course')

        available, earned = 0.0, 0.0

        for result in results:
            available += result.assignment.possible_mark
            earned += result.mark

        # calculations for progress bar
        if available != 0:
            percentage_complete = int(round(earned / available * 100, 0))
        else:
            percentage_complete = 0

        earned = int(earned)
        available = int(available)

        return render(request, 'home.html', {'available': available, 'earned': earned,
                                             'percentage': percentage_complete,
                                             'results': results,})
    else:
        return HttpResponseRedirect("../login")