from django.conf.urls import url

from MyWebsite import views
from MyWebsite.views import RecruiterListView

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^student/$', views.student, name='student'),
    url(r'^recruiter/$', views.recruiter, name='recruiter'),
    url(r'^about/$', views.about, name='about'),
    url(r'^procedure/$', views.procedure, name='procedure'),
    url(r'^academic/$', views.academic, name='academic'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^department/$', views.department, name='department'),
    url(r'^recruiter/form$', views.recruiter_form, name='recruiter_form'),
    url(r'^beyond-academic$', views.beyond_academic, name='beyond_academic'),
    url(r'^addBeyondAcademicimage/$',views.AddBeyondAcademicimages,name='addBeyondAcademicimages'),
    url(r'^addPastRecruiterimage/$',views.addPastRecruiterimage,name='addPastRecruiterimage'),
    url(r'^addBeyondAcademicvideos/$',views.AddBeyondAcademicvideos,name='addBeyondAcademicvideos'),
    url(r'^addBeyondAcademichighlight/$',views.AddBeyondAcademicHighlight,name='addBeyondAcademichighlight'),
    url(r'^addinterndescrip/$',views.Addinterndescrip,name='addinterndescrip'),
    url(r'^addngodescrip/$',views.Addngodescrip,name='addngodescip'),
    url(r'^change_password/$',views.change_password,name='change_password'),
    url(r'^college-team/$',views.college_team,name='college_team'),
    url(r'^alumni/$',views.alumni,name='alumni'),
    url(r'^research-development/$',views.research_development,name='research_development'),
    url(r'^studentapply/(?P<pk>[\w\-]+)/$',views.studentapply,name='studentapply'),
    url(r'^recruiter-list/$',views.RecruiterListView,name='recruiterlist'),
    ]