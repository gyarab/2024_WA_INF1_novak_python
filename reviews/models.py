from django.db import models
from games.models import Game
from users.models import User

class GameReview(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    submission_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Review by {self.user} for {self.game.name} - {self.rating} Stars"

    class Meta:
        ordering = ['-created_at']
