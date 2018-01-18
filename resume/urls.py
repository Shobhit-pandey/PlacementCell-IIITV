from django.conf.urls import patterns, url
from wkhtmltopdf.views import PDFTemplateView

from resume import views
from resume.views import ResumePdf

urlpatterns = [
    url(r'^resume/delete/$', views.delete_resume, name='delete_resume'),
    url(r'^create-resume/(?P<pk>[\w\-]+)/$', views.createresume, name='createresume'),
    url(r'^(?P<pk2>[\w\-]+)/$', views.resume, name='resume'),
    url(r'^(?P<pk4>[\w\-]+).pdf/$', views.html_to_pdf_view, name='pdf'),
]
