from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

STATUS_CHOICES = {
    ('To Read', 'To Read'),
    ('Reading', 'Reading'),
    ('Already Read', 'Already Read'),
}

class User(AbstractUser):
    pass

class Book(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='')

    # def __str__(self):
    #     return self.title


class Note(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='notes')
    note_text = models.TextField(max_length=1000, blank=True, null=True)
    date_time = models.DateField(auto_now_add=True)
    page_number = models.CharField(max_length=20, blank=True, null=True)

def get_available_books_for_user(queryset, user):
    if user.is_authenticated:
        books = queryset.filter(Q(user=user))
    else:
        books = None
    return books

# def get_available_notes_for_book(queryset, user, book):
#     if user.is_authenticated:
#         notes = queryset.filter(Q(book=book) | Q(user=user))
#     else: 
#         notes = None
#     return notes