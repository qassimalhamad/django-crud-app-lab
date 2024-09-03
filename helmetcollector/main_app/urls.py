from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('helmets/', views.helmet_index, name='helmet-index'),
    path('helmets/<int:helmet_id>/', views.helmet_detail, name='helmet-detail'),
    path('helmets/create/', views.HelmetCreate.as_view(), name='helmet-create'),
    path('helmets/<int:pk>/update/', views.HelmetUpdate.as_view(), name='helmet-update'),
    path('helmets/<int:pk>/delete/', views.HelmetDelete.as_view(), name='helmet-delete'),
    path('helmets/<int:helmet_id>/add-brand/', views.add_brand, name='add-brand'),
    path('helmets/<int:helmet_id>/brand/add/', views.BrandCreate.as_view(), name='brand-create'),
    path('brands/<int:pk>/update/', views.BrandUpdate.as_view(), name='brand-update'),
    path('brands/<int:pk>/delete/', views.BrandDelete.as_view(), name='brand-delete'),
    
]