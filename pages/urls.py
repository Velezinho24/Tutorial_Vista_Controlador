from django.urls import path
from . import views
from .utils import ImageLocalStorage

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('contact/', views.ContactPageView.as_view(), name = 'contact'),
    path('products/', views.ProductIndexView.as_view(), name='index'),
    path('products/create', views.ProductCreateView.as_view(), name='form'),
    path('products/<str:id>/', views.ProductShowView.as_view(), name='show'),
    path('cart/', views.CartView.as_view(), name='cart_index'),
    path('cart/add/<str:id>/', views.CartView.as_view(), name='cart_add'),
    path('cart/removeAll', views.CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', views.ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'), 
    path('image/save', views.ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('imagenotdi/', views.ImageViewNoDI.as_view(), name='imagenodi_index'),
    path('imagenotdi/save', views.ImageViewNoDI.as_view(), name='imagenodi_save'),
]