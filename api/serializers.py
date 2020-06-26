from django.shortcuts import render
from .models import User, Book, Note
from rest_framework import serializers

# Create your views here.

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'url', 'username',]

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    
    
    class Meta:
        model = Note
        fields = [
            'note_text', 'book', 'page_number',
        ]

class BookSerializer(serializers.HyperlinkedModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = [
            'url', 'user', 'title', 'author', 'status', 'notes',
        ]
    
    