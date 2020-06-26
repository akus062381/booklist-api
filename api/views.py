from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, Book, Note, get_available_books_for_user
from .serializers import UserSerializer, BookSerializer, NoteSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import filters

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    # define get_queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        queryset = get_available_books_for_user(Book.objects.all(), self.request.user)

        return queryset

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date_time']

    # def get_queryset(self):
    #     queryset = get_available_notes_for_book(Note.objects.all(), self.request.user)

    #     return queryset

    # look at recipebook code permissions 
  