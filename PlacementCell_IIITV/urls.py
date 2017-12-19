"""PlacementCell_IIITV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_complete, \
    password_reset_confirm

import MyWebsite

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^', include('MyWebsite.urls', namespace="mywebsite")),
    url(r'^student/login/$',views.login,{'template_name':'Student.html'},name='studentlogin'),
    url(r'^recruiter/login/$',views.login,{'template_name':'Recruiter.html'},name='recruiterlogin'),
    url(r'^accounts/logout/$',views.logout,name = 'logout', kwargs = {'next_page':'/'}),
    url(r'^reset-password/$',password_reset,name='reset_password'),
    url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,name='password_reset_confirm'),
    url(r'^reset-password/complete/$',password_reset_complete,name='password_reset_complete'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
