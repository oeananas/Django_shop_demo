from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product'),
]
