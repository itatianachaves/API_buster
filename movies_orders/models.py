from django.db import models

class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_order",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_order",
    )
