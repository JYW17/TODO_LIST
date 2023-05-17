from django.urls import path
from . import views
from .models import Todo
from .forms import TodoForm
from django.shortcuts import render, redirect

# Create your views here.
def todoList(request):
    todos = Todo.objects.filter(completed=False)
    return render(request, 'todoApp/todoList.html', {'todos': todos})

def todoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todoApp/todoDetail.html', {'todo': todo})

def todoPost(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todoList')
    else:
        form = TodoForm()
    return render(request, 'todoApp/todoPost.html', {'form': form})


def todoEdit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todoList')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoApp/todoPost.html', {'form': form})

def todoDone(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.save()
    return redirect('todoList')


def todoDoneList(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, 'todoApp/todoDoneList.html', {'dones': dones})

def todoDeleteFromList(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todoList')

def todoDeleteFromDone(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todoDoneList')