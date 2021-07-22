from django.urls import path

from . import views

app_name = 'craigsearch'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:searchquery_id>/', views.searchresults, name='searchresults'),
]
