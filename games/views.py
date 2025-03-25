from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, Category
from .forms import GameForm
from django.utils import timezone

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

@login_required
def game_list_by_publisher(request):
    games = Game.objects.filter(publisher=request.user)
    return render(request, 'games/game_list.html', {'games': games})

@login_required
def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'games/game_detail.html', {'game': game})

@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.publisher = request.user
            game.ip_address = request.META.get('REMOTE_ADDR')
            game.user_agent = request.META.get('HTTP_USER_AGENT')
            game.submission_time = timezone.now()
            game.save()
            form.save_m2m()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'games/game_form.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        if category_name:
            Category.objects.get_or_create(name=category_name)
        return redirect('add_game')

    return render(request, 'games/category_form.html')


@login_required
def edit_game(request, slug):
    game = get_object_or_404(Game, slug=slug, publisher=request.user)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'games/game_form.html', {'form': form})

@login_required
def delete_game(request, slug):
    game = get_object_or_404(Game, slug=slug, publisher=request.user)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})
