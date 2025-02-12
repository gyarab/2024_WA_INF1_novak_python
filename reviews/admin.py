from django.contrib import admin
from .models import GameReview

@admin.register(GameReview)
class GameReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('game__name', 'user__name', 'content')
