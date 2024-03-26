from rest_framework.generics import ListAPIView
from .serializers import TaskSerializer
from .models import TaskModel
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class ListTaskAPIView(ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['task_name']
    ordering_fields = ['task_name']
    
    class CustomPagination(PageNumberPagination):
        page_size = 1
        page_query_param = 'page_size'
        max_page_size = 3
        
    pagination_class = CustomPagination
    

