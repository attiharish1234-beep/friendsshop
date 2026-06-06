from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/', views.product),
    path('save-order/', views.save_order),
    path('payment/', views.payment),
    path('success/', views.success),
]