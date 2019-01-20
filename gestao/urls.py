from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('animais/', views.list_animais),
    path('animais/<int:animal_id>/', views.show_animal),
    path('fazendeiros/', views.list_fazendeiros)
]
