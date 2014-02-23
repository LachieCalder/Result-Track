from django.shortcuts import render
from django.http import HttpResponseRedirect

def about(request):
    return render(request, 'static/about.html', {'title': 'About'})

