from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<city_name>/', views.delete_city, name = 'delete_city'),
    path('_', views.delete_everything, name = 'delete_everything'),
    path('', views.map, name='map')
]
