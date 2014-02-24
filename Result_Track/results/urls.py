from django.conf.urls import patterns, url
from results import views
from django.contrib.auth.views import login

urlpatterns = patterns('',
    url(r'^about/', views.about, name="about"),
    url(r'^login/', login, {'template_name': 'login.html', 'redirect_field_name': 'http://127.0.0.1:8000/accounts/profile/'}),
    url(r'^home/', views.home, name="home")
)