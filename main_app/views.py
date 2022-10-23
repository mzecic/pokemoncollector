from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Pokemon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, pokemon_type, description, height):
    self.name = name
    self.pokemon_type = pokemon_type
    self.description = description
    self.height = height

pokemon = [
  Pokemon('Caterpie', 'bug', 'worm pokemon', 1),
  Pokemon('Evee', 'normal', 'mammalian, quadrupedal pokemon', 1),
  Pokemon('Togepi', 'normal', 'spikeball', 1)
]

def home(request):
    return HttpResponse('<h1>Hello ϞϞ(๑⚈ ․̫ ⚈๑)∩</h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })
