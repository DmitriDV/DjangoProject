from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    #tasks = Task.objects.all() - all objects
    tasks = Task.objects.order_by('-id') [:7] # 7 objects on the page will sorted by id from old to new.
    return render(request, 'main/index.html', {'title': "Page Accueil", 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('homePage')
        else:
            error = 'Les données ne sont pas remplies correctement'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
