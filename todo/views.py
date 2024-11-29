from django.shortcuts import render
from rest_framework import viewsets
from .serialisers import TodoSelializer
from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSelializer
    queryset = Todo.objects.all()