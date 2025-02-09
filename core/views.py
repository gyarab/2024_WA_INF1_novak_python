from django.shortcuts import render
from games.models import Game

def home(request):
    # Fetch featured games (for example, the most recent or top-rated games)
    featured_games = Game.objects.all()[:6]  # Change this to fetch based on your criteria
    return render(request, 'core/home.html', {'featured_games': featured_games})
