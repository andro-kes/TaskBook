from django.db import models

class TagModel(models.Model):
    color_list = (
        ('красный', 'красный'),
        ('синий', 'синий'),
        ('желтый', 'желтый'),
        ('зеленый', 'зеленый'),
    )
    
    tag_name = models.CharField(max_length=50)
    color = models.CharField(max_length=10, choices=color_list)

class TaskModel(models.Model):
    category_list = (
        ('очень важно', 'очень важно'),
        ('важно', 'важно'),
        ('желательно', 'желательно'),
        ('мечтаю', 'мечтаю'),
    )
    
    task_name = models.CharField(max_length=250)
    category = models.CharField(max_length=20, choices=category_list)
    tag = models.ForeignKey(TagModel, on_delete=models.CASCADE)
