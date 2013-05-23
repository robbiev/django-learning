from django.conf.urls import patterns, url
from app1 import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
#  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^new/$', views.new_reservation, name='new_reservation'),
  url(r'^save/$', views.save_reservation, name='save_reservation'),
#  url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
#  url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
#
#  # /poll/5
#  url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#  # /polls/5/results/
#  url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#  # /polls/5/vote/
#  url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
