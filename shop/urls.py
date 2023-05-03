from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('items', views.ItemsView.as_view(), name='items'),
    path('vendors', views.VendorsView.as_view(), name='vendors'),
    path('stockin', views.StockinView.as_view(), name='stockin'),
    path('stockout', views.StockOutView.as_view(), name='stockout'),
    # path('item_create/<int:pk>', views.ItemCreateView.as_view(), name='item_create'),

]