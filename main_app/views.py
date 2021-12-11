from django.shortcuts import render

# Create your views here.
import requests


def home(request):
    #get the list of todos
    response=requests.get('https://jsonplaceholder.typicode.com/users/')

    todos=response.json()
    #transfer the response to json object

    return render(request, 'main_app/todos.html', {'todos':todos})

