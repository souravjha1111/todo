from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        '/api': 'list of things available',
        'task-list': 'gives you all tasks list availabe database',
        'task-create/': 'Post a tak through jaseon format just copy this and edit as per requirements => {"id": 5, "title": "hi", "completed": false  }',
        'task-details/id': 'for specific task details',
        'task-Update/id': 'update any id value',
        'task-Delete/id': 'Delete any id value...click that red button too',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer =TaskSerializer(tasks, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer =TaskSerializer(tasks, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer =TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer =TaskSerializer(instance = tasks, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id = pk)
    tasks.delete()
    return Response("DEleted subject")