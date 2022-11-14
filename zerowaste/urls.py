from django.urls import path
from . import views
urlpatterns = [
    path('', views.base),
    path('shop_search/', views.search, name='search_result'),
    path('shop_info/', views.info, name="info_result"),
    path('detail/<int:id>', views.shop_detail, name="shop_detail"),
]
