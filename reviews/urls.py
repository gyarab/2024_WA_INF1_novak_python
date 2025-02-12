from django.urls import path
from .views import add_review, delete_review

urlpatterns = [
    path('add/<str:game_slug>/', add_review, name='add_review'),
    path('delete/<int:review_id>/', delete_review, name='delete_review'),
]
