from django.conf.urls import patterns, url

from quiz import views
from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, QuizRecruiterMarkingList

urlpatterns = patterns('',
                       url(regex=r'^$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),

                       url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                       url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                       url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                       url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                       url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),

                       url(r'^create/quiz/$',views.Createquiz,name='createquiz'),
                       url(r'^add/question/$',views.Createquestion,name='createquestion'),
                       url(r'^add/mcq/$',views.AddMcq,name='addmcq'),
                       url(r'^add/tf/$',views.AddTF,name='addtf'),
                       url(r'^add/essay/$',views.AddEssay,name='addessay'),
                       url(r'^create/category$',views.CreateCategory,name='createcategory'),
                       url(r'^recruiter/quiz/cateogerylist/(?P<quiz_name>[\w|\W-]+)/$', QuizRecruiterMarkingList.as_view(), name='recruitermarkinglist'),

)
