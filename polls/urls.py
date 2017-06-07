from django.conf.urls import url

from polls import views

urlpatterns=[
    url(r'^$', views.QuestionListView.as_view(), name="home"),
    url(r'^(?P<pk>[0-9]+)/$', views.QuestionDetailView.as_view(), name="view"),
    url(r'^(?P<id>[0-9]+)/result/$', views.question_result, name="result"),
    url(r'^(?P<id>[0-9]+)/vote/$', views.question_vote),
]