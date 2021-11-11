from django.urls import path
from .views import ProductListView, ProductDetailView
from . import views

urlpatterns = [
    # path('', views.home, name='alexadashcams-home'),
    path('about/', views.about, name='alexadashcams-about'),
    path('', ProductListView.as_view(), name='alexadashcams-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

]

