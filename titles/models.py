from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Role(models.TextChoices):
        user = 'user', _('user')
        moderator = 'moderator', _('moderator')
        admin = 'admin', _('admin')

    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=128, blank=True)
    role = models.CharField(
        max_length=9,
        choices=Role.choices,
        default=Role.user
    )
    bio = models.CharField(max_length=30, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField(blank=True, verbose_name='Year')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='title', blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    description = models.TextField(max_length=300, blank=True)


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name="reviews")
    text = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="reviews")
    score = models.DecimalField(decimal_places=1, max_digits=3)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'author')


class Comments(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="comments")
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    pub_date = models.DateTimeField(auto_now_add=True)
