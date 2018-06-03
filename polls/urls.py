from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #127.0.0.1
    path('<int:question_id>/', views.detail, name='detail'),
    #127.0.0.1/1        
    path('<int:question_id>/results/', views.results, name='result'),
    #127.0.0.1/1/result
    path('<int:question_id>/vote/', views.vote, name='vote')
    #127.0.0.1/1/vote
]
