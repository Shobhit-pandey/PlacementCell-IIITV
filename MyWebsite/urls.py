from django.conf.urls import url

from MyWebsite import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^student/$', views.student, name='student'),
    url(r'^recruiter/$', views.recruiter, name='recruiter'),
    ]