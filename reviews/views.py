from django.shortcuts import render, get_object_or_404, redirect
from .models import GameReview
from games.models import Game
from .forms import GameReviewForm

def add_review(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    if request.method == "POST":
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.game = game
            review.save()
            return redirect('game_detail', slug=game.slug)
    else:
        form = GameReviewForm()
    
    return render(request, 'reviews/add_review.html', {'form': form, 'game': game})

def delete_review(request, review_id):
    review = get_object_or_404(GameReview, id=review_id)
    if request.user == review.user:
        review.delete()
    return redirect('game_detail', slug=review.game.slug)
