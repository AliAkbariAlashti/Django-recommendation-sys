from django.urls import path
from . import views



urlpatterns = [
    path('recommendation', views.recommender.as_view()),
    path('newuser', views.newuser),
    path('userinterestsform', views.home)
]
