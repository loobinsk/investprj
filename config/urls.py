from django.contrib import admin
from django.urls import path
from . import views
from . import client_views
from . import account_views
from . import system_views



urlpatterns = [
    path('', views.index, name='homepage'),
    path('algoritm/', system_views.get_algorithm),
    path('create-portfolio/', views.create_portfolio, name='create-portfolio'),
    path('client-delete/<pk>/', client_views.client_delete, name='client-delete'),
    path('client-change/<pk>/', client_views.client_change, name='client-change'),
    #path('clients/', views.clients_list, name='clients'),
    path('client-overview/<pk>/', client_views.client_detail, name='client-overview'),
    path('client-overview/', client_views.clients_list, name='clients-list'),
    path('portfolio-view/<pk>/', views.portfolio_view, name='portfolio-view'),
    path('portfolio_detail/<pk>/', views.portfolio_detail, name='portfolio_detail'),

    #path('portfolio-overview', views.portfolio_detail, name='portfolio-overview'),
    path('change-pass/', account_views.change_pass, name='change-pass'),
    path('new-client/', client_views.new_client, name='new-client'),
    path('settings/', account_views.settings, name='settings'),
    path('register/', account_views.register, name='register'),
    path('login/', account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
    path('admin/', admin.site.urls),
    path('add_shares_in_db/', system_views.add_data_for_all_shares_to_the_internal_database, name='asid'),
    path('test/', system_views.logic_test),
]
