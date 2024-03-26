from rest_framework.generics import ListAPIView
from .serializers import TaskSerializer
from .models import TaskModel
from rest_framework import filters

class ListTaskAPIView(ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['task_name']
    ordering_fields = ['task_name']
    
    

