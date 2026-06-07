from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', views.home, name='home'),

    # Product page
    path('product/<int:id>/', views.product, name='product'),

    # Payment flow
    path('save-order/', views.save_order, name='save_order'),
    path('payment/', views.payment, name='payment'),
    path('success/', views.success, name='success'),
]

# MEDIA FILES (IMPORTANT for images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)