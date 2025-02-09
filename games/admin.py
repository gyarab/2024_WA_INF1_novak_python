from django.contrib import admin
from .models import Game, Category

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'publisher', 'release_date')
  list_filter = ('publisher', 'categories')
  search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
