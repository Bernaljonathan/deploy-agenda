from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'todos':todos
    }
    return render(request, 'todo/index.html', context)


def view(request,id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request, 'todo/detail.html', context)


def edit(request,id):
    return render(request, 'todo/index.html', {})


def create(request):
    
    if request.metod == 'GET':
        form = TodoForm() 
        context = {
            'form':form
        }
        return render(request, 'todo/index.html', context)
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')


def delete(request,id):
    return render(request, 'todo/index.html',{})
    