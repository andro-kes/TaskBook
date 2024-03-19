from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import TaskModel

class ListTaskAPIView(ListAPIView):
    model = TaskModel
    queryset = TaskModel.objects.all()
