from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view', views.login_view, name='login_view'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('card', views.card, name='card'),
    path('card_view', views.card_view, name='card_view'),
    path('card_update/<int:id>/', views.card_update, name='card_update'),
    path('card_delete/<int:id>/', views.card_delete, name='card_delete'),
]