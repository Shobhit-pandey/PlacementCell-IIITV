from django.conf.urls import url

from MyWebsite import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    ]