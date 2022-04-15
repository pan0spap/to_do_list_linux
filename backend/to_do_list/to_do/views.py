from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def tasks_list(request):
    if request.method == 'GET':
        content = ToDoTask.objects.all()
        serializer = TaskSerializer(content, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:    
            return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def tasks_detail(request, pk):
    if request.method == 'GET':
        try:
            content = ToDoTask.objects.get(pk=pk)
        except ToDoTask.DoesNotExist:
            return Response({'Error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)    

        serializer = TaskSerializer(content)
        return Response(serializer.data)


    if request.method == 'PUT':
        content = ToDoTask.objects.get(pk=pk)
        serializer = TaskSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        content = ToDoTask.objects.get(pk=pk)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            


