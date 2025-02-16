from django.shortcuts import render
from games.models import Game

def home(request):
    featured_games = Game.objects.all().order_by('-release_date')[:3]
    return render(request, 'core/home.html', {'featured_games': featured_games})
