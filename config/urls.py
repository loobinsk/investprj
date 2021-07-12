from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('algoritm/', views.get_algorithm),
    path('create-portfolio/', views.create_portfolio, name='create-portfolio'),
    path('client-delete/<pk>/', views.client_delete, name='client-delete'),
    #path('clients/', views.clients_list, name='clients'),
    path('client-overview/<pk>/', views.client_detail, name='client-overview'),
    path('client-overview/', views.clients_list, name='clients-list'),
    path('portfolio-view/<pk>/', views.portfolio_view, name='portfolio-view'),
    #path('portfolio-overview', views.portfolio_detail, name='portfolio-overview'),
    path('change-pass/', views.change_pass, name='change-pass'),
    path('new-client/', views.new_client, name='new-client'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]
