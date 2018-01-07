from django.conf.urls import patterns, url

from resume import views

urlpatterns = [
    url(r'^create-resume/(?P<pk>[\w\-]+)/$',views.createresume,name='createresume'),
    url(r'^resume/(?P<pk2>[\w\-]+)/$',views.resume,name='resume'),
]