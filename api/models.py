from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE)
    rating = models.PositiveSmallIntegerField()
