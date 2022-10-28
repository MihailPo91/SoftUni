from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        validators=(MinValueValidator(12),),
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    GAME_CATEGORIES = [("Action", "Action"),
                       ("Adventure", "Adventure"),
                       ("Puzzle", "Puzzle"),
                       ("Strategy", "Strategy"),
                       ("Sports", "Sports"),
                       ("Board/Card Game", "Board/Card Game"),
                       ("Other", "Other")]
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )
    category = models.CharField(
        choices=GAME_CATEGORIES,
        null=False,
        blank=False,
        max_length=15
    )
    rating = models.FloatField(
        validators=(MinValueValidator(0.1), MaxValueValidator(5.0)),
        null=False,
        blank=False,
    )
    max_level = models.PositiveIntegerField(
        validators=(MinValueValidator(1),),
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
