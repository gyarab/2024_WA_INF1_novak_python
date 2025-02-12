from django import forms
from .models import GameReview

class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
