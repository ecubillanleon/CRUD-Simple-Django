from django.shortcuts import render, redirect
from .models import TasksModel

# Create your views here.
def lista_tasksView(request):
    tasks = TasksModel.objects.all()
    return render(request, 'lista_tasks.html', {"tasks": tasks})


def create_tasksView(request):
    tasks = TasksModel(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    tasks.save()
    return redirect('/tasks/')


def delete_tasksView(request, tasks_id):
    task = TasksModel.objects.get(id=tasks_id)
    task.delete()
    return redirect('/tasks/')