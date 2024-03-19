from rest_framework.generics import ListAPIView
from .serializers import TaskSerializer
from .models import TaskModel

class ListTaskAPIView(ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    

