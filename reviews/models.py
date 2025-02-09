from django.db import models
from users.models import User
from games.models import Game

class GameReview(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review of {self.game.name} by {self.user.username}"
    
    def save(self, *args, **kwargs):
        if not (1 <= self.rating <= 10):
            raise ValueError("Rating must be between 1 and 10")
        super().save(*args, **kwargs)