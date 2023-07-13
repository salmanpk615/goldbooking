from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('home', views.index, name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='shop/registration/login.html'), name='login'),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path('logout', auth_views.LogoutView.as_view(template_name='shop/registration/login.html'), name='logout'),
    path('items', views.ItemsView.as_view(), name='items'),
    path('item_delete/<int:pk>', views.ItemDelete.as_view(), name='item_delete'),
    path('item_update/<int:pk>', views.ItemEdit.as_view(), name='item_update'),
    path('vendors', views.VendorsView.as_view(), name='vendors'),
    path('vendor_delete/<int:pk>', views.VendorDelete.as_view(), name='vendor_delete'),
    path('vendor_update/<int:pk>', views.VendorEdit.as_view(), name='vendor_update'),
    path('stockin', views.StockinView.as_view(), name='stockin'),
    path('stockin_delete/<int:pk>', views.StockinDelete.as_view(), name='stockin_delete'),
    path('stockin_update/<int:pk>', views.StockinEdit.as_view(), name='stockin_update'),
    path('stockout', views.StockOutView.as_view(), name='stockout'),
    path('stock_update/<int:pk>', views.StockOutEdit.as_view(), name='stock_update'),
    path('stockout_delete/<int:pk>', views.StockoutDelete.as_view(), name='stockout_delete'),
    path('slip/<int:pk>/', views.slip_view, name='slip'),
    path('slip_out/<int:pk>/', views.slip_out, name='slip_out'),
    path('reports', views.ReportsView.as_view(), name='reports'),
    path('report_update/<int:pk>', views.ReportEdit.as_view(), name='report_update'),
    path('report_delete/<int:pk>', views.ReportDelete.as_view(), name='report_delete'),
    path('pdf/<int:pk>', views.pdf_view, name='pdf'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('item_detail/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
]