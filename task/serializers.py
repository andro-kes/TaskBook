from rest_framework import serializers
from .models import TaskModel, TagModel

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('tag_name', 'color')

class TaskSerializer(serializers.ModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(queryset=TagModel.objects.all())
    
    class Meta:
        model = TaskModel
        fields = ('task_name', 'category', 'tag')
        
