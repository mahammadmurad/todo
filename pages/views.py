from django.shortcuts import render
from .models import *
import datetime

def index(request):
    return render (request, 'index.html')


def add(request):
    alltodos = Todo.objects.all()
    obj = Todo()

    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    obj.created_at = request.POST['time']
    obj.save()

    context = {
        'alltodos': alltodos
    }

    return render(request, 'list.html', context)



def delete(request, id):
    alltodos = Todo.objects.all()
    obj = Todo.objects.get(id=id)

    obj.delete()

    context= {
        'alltodos':alltodos
    }

    return render (request, 'list.html', context)


def search(request):
    src = request.POST['query']

    alltodos= Todo.objects.filter(title__contains=src)

    context = {
        'alltodos':alltodos
    }

    return render(request, 'list.html' , context)

def edit(request, id):
    
    obj = Todo.objects.get(id=id)
    
    title = obj.title
    description = obj.description
    priority = obj.priority
    time = obj.created_at
    id = obj.id
    

    context = {
        'title': title,
        'description': description,
        'priority': priority,
        'id': id,
        'time': time
    }

    return render(request, 'edit.html', context)

def update(request, id):
    alltodos = Todo.objects.all()
    obj = Todo(id=id)

    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.priority = request.POST['priority']
    obj.created_at = request.POST['time']

    updated_at = datetime.datetime.now()
    
    obj.created_at = updated_at

    obj.save()

    context = {
        'alltodos': alltodos
    }
    
    return render(request, 'list.html', context)


def list(request):
    alltodos = Todo.objects.all()

    context = {
        'alltodos': alltodos
    }

    return render(request, 'list.html', context)
    









# Create your views here.
