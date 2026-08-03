from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="posters/")
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=300)
    rating = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="movies"
    )
    youtube_link = models.URLField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    def __str__(self):
        return self.title