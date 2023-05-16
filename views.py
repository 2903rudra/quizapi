# from django.shortcuts import render
from rest_framework import generics
from.models import Quiz
from .serializers import Quizserializer

# Create your views here.

class QuizeCreativeAPIView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = Quizserializer

class QuizRetrievUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = Quizserializer