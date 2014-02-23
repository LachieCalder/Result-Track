from django.conf.urls import patterns, url
from results import views
from django.contrib.auth.views import login

urlpatterns = patterns('',
    url(r'^register/'), views.re
    url(r'^about/', views.about, name="about"),
    url(r'^login/', login, {'template_name':'login.html'})
)