from django.urls import path
from .views import game_list, game_list_by_publisher, game_detail, add_game, add_category, edit_game, delete_game

urlpatterns = [
    path('', game_list, name='game_list'),
    path('my/', game_list_by_publisher, name='game_list_by_publisher'),
    path('add/', add_game, name='add_game'),
    path('add-category/', add_category, name='category_create'),
    path('<slug:slug>/', game_detail, name='game_detail'),
    path('<slug:slug>/edit/', edit_game, name='edit_game'),
    path('<slug:slug>/delete/', delete_game, name='delete_game'),
]
