from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.username

class VideoGame(models.Model):
    name= models.CharField(max_length=120)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_game = models.ForeignKey(VideoGame, on_delete=models.CASCADE )
    star_rating = models.IntegerField(default=0, validators=[
        MaxValueValidator(5), MinValueValidator(0)
    ])
    comment = models.TextField()
    location = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.user
