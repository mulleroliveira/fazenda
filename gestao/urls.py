from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('animais/', views.animais_list),
    path('animais/<int:animal_id>/', views.animal_show),
    path('animais/form/', views.animal_form),
    path('animais/<int:animal_id>/edit/', views.animal_edit),
    path('fazendeiros/', views.fazendeiros_list),
    path('fazendeiros/<int:fazendeiro_id>/', views.fazendeiro_show),
    path('fazendeiros/form/', views.fazendeiro_form),
]
