from django.http import HttpResponse
from django.shortcuts import render
from .models import Animal
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


def create_animal(request):
    a = Animal.objects.create(name='horse', age=10)
    return HttpResponse("Hello, world. You're at the polls index.")

