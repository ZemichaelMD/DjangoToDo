from django.shortcuts import render, redirect
#from django.http import HttpResponse


from .models import *
from .forms import *


# Create your views here.
def index(request):
    title = "Zee's Todo List"

    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form, 'title': title}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    title = "Updating: " + str(Task.objects.get(id=pk))
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'title':title}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    title = "Deleting: " + str(Task.objects.get(id=pk))

    task = Task.objects.get(id=pk)

    context={'task': task, 'title':title}

    if request.method=="POST":
        task.delete()
        return redirect("/")

    return render(request, 'tasks/delete.html', context)