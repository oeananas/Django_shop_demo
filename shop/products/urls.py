from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
