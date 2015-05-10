__author__ = 'Robert Waltham'
from django.conf.urls import patterns, url

from DotaStats import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view() , name='index'),
    url(r'^load-matches/$', views.LoadMatchesFromAPI.as_view(), name='load-matches'),
    url(r'^process-match/$', views.LoadDetailsForAll.as_view(), name='process-match'),
    url(r'^load-static-data/$', views.LoadStaticDataView.as_view(), name='static-data'),
    url(r'^hero/(?P<pk>\d+)/', views.HeroDetail.as_view(), name='hero-detail'),
    url(r'^match/(?P<pk>\d+)/', views.MatchDetail.as_view(), name='match-detail'),
    url(r'^build/', views.BuildDataView.as_view(), name='build-data'),
    url(r'^test/', views.BuildAndTestView.as_view(), name='build-test'),
    url(r'^items/', views.ItemListView.as_view(), name='items'),
    url(r'^heroes/', views.HeroListView.as_view(), name='heroes'),
    url(r'^matches/', views.MatchList.as_view(), name='matches'),
    url(r'^predict/', views.CreatePredictionView.as_view(), name='create_prediction'),
    url(r'^login/', views.LogInView.as_view(), name='login'),
    url(r'^logout/', views.LogOutView.as_view(), name='logout'),

)