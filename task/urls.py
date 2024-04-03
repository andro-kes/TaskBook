from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTaskAPIView.as_view(), name='list_task'),
    path('<int:id>', views.DetailTask.as_view(), name='detail'),
    path('tag', views.TagCreateList.as_view(), name='list_tag'),
]
