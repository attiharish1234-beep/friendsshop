from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('slippers/', views.slippers),
    path('sandals/', views.sandals),
    path('footwear/', views.footwear),
]