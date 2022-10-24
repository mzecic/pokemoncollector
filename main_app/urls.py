from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='index'),
    path('pokemon/<int:pokemon_id>', views.pokemon_detail, name='detail'),
    path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
]
