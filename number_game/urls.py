from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('correct', views.correct),
    path('too_high', views.too_high),
    path('too_low', views.too_low),
]