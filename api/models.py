from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class VideoGame(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="uploads/")
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    star_rating = models.IntegerField(
        default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    comment = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.video_game
