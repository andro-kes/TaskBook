from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTaskAPIView.as_view(), name='list_task'),
]
