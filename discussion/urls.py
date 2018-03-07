from django.conf.urls import url

from discussion import views

urlpatterns = [
    url(r'^$', views.share, name='share'),
    url(r'^add/$', views.add_share, name='add_share'),
    url(r'^replies/(?P<pk>\d+)/$', views.sharecomments, name='replies'),
    url(r'^reply/$', views.sharecomment, name='reply'),
    url(r'^delete-share/(?P<pk1>\d+)/$', views.deleteshare, name='deleteshare'),
    url(r'^delete-reply/(?P<pk2>\d+)/$', views.deletereply, name='deletereply'),
]
