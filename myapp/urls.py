from django.urls import path
from myapp import views
from django.conf.urls import url



urlpatterns = [
    path('',views.IndexFunc),
    path('index',views.IndexFunc),
    path('search/',views.SearchFunc),
    path('analysis/',views.analysisFunc),
    path('topplayer/',views.topplayerFunc),
    path('topplayer/TOPatk',views.TOPatkFunc),
    path('topplayer/TOPmid',views.TOPmidFunc),
    path('topplayer/TOPdef',views.TOPdefFunc),
    
    path('testtem',views.testtem),

 
    url(r'^ajaxproject/$', views.ajaxproject),  
    url(r'^searchData/$', views.searchData), 
    url(r'^squadform/$', views.squadform), 
    url(r'^Mysquadform/$', views.Mysquadform), 
    url(r'^recommend/$', views.recommend),  
    url(r'^takeplayer/$', views.take),  
      
]
