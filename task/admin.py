from django.contrib import admin
from .models import TaskModel, TagModel

admin.site.register(TaskModel)
admin.site.register(TagModel)
