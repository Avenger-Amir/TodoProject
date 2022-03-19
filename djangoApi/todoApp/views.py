from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from todoApp.models import Todo, NewUserForm
from todoApp.serealizers import TodoSerealizers, NewUserFormSerealizers
# Create your views here.

@csrf_exempt
def todoApi(request,id = 0):
    if request.method =='GET':
        todos = Todo.objects.all()
        todo_serializer = TodoSerealizers(todos, many = True)
        return JsonResponse(todo_serializer.data, safe=False)
    elif request.method == 'POST':
        todo_data=JSONParser().parse(request)
        todo_serializer = TodoSerealizers(data = todo_data)
        print(todo_serializer)
        print(todo_serializer.is_valid())
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Added Successfully!!", safe = False)
        return JsonResponse("Failed to Add", safe = False)

    elif request.method == 'PUT':
        todo_data = JSONParser().parse(request)
        todo = Todo.objects.get(id = todo_data['id'])
        todo_serializer = TodoSerealizers(todo,data = todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Updated Successfully!!", safe = False)
        return JsonResponse("Failed to Update", safe = False) 

    elif request.method == 'DELETE':
        todo_data = Todo.objects.get(id = id)
        todo_data.delete()
        return JsonResponse("Deleted Successfully!!", safe = False)


@csrf_exempt
def signUp(request):
    if request.method =='GET':
        users = NewUserForm.objects.all()
        user_serializer = NewUserFormSerealizers(users, many = True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data=JSONParser().parse(request)
        user_serializer = NewUserFormSerealizers(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!!", safe = False)
        return JsonResponse("Failed to Add", safe = False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = NewUserForm.objects.get(id = user_data['id'])
        user_serializer = NewUserFormSerealizers(user,data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!!", safe = False)
        return JsonResponse("Failed to Update", safe = False) 

    elif request.method == 'DELETE':
        user_data = Todo.objects.get(id = id)
        user_data.delete()
        return JsonResponse("Deleted Successfully!!", safe = False)

