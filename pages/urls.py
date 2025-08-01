from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('contact/', views.ContactPageView.as_view(), name = 'contact'),
    path('products/', views.ProductIndexView.as_view(), name='index'),
    path('products/<str:id>/', views.ProductShowView.as_view(), name='show'),
]