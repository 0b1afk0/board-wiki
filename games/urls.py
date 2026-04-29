from django.urls import path
from . import views

urlpatterns = [
    path('', views.g_list, name='g_list'),
    path('g/<int:game_id>/', views.g_detail, name='g_detail'),
]