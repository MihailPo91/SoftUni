from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app_exam.music.validators import validate_if_value_contains_only_nums_chars_and_underscore, \
    validate_value_is_above_zero


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(MinLengthValidator(2),
                    validate_if_value_contains_only_nums_chars_and_underscore,),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        # validators=(validate_value_is_above_zero,),
    )


class Album(models.Model):
    # GENRE_CHOICES = ((1, "Pop Music"), (2, "Jazz Music"), (3, "R&B Music"), (4, "Rock Music"), (5, "Country Music"),
    #                  (6, "Dance Music"), (7, "Hip Hop Music"), (8, "Other"))
    GENRE_CHOICES = (("Pop Music", "Pop Music"), ("Jazz Music", "Jazz Music"), ("R&B Music", "R&B Music"), ("Rock Music", "Rock Music"), ("Country Music", "Country Music"),
                     ("Dance Music", "Dance Music"), ("Hip Hop Music", "Hip Hop Music"), ("Other", "Other"))
    album_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )
    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=GENRE_CHOICES
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        validators=(validate_value_is_above_zero,),

    )
    # TODO The number of decimal places of the price should not be specified in the database
