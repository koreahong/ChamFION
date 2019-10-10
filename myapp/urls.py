from django.urls import path
from myapp import views
from django.conf.urls import url



urlpatterns = [
    path('',views.IndexFunc),
    path('index',views.IndexFunc),
    path('search/',views.SearchFunc),
 
    url(r'^ajaxproject/$', views.ajaxproject),  
    url(r'^searchData/$', views.searchData), 
    url(r'^squadform/$', views.squadform), 
    url(r'^recommend/$', views.recommend),  
      
]
