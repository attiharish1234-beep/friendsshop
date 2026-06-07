from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product, name='product'),
    path('save-order/', views.save_order, name='save_order'),
    path('payment/', views.payment, name='payment'),
]