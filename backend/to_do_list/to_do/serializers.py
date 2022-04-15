from .models import *
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = '__all__'