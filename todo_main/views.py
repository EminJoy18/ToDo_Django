from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False) # only unfinished tasks
    # .filter().order_by('updated_at') = to order the added tasks => This is in ascending order of updated time
    # "-updated_at" => indicates descending order
    compltd_tasks = Task.objects.filter(is_completed=True)
    context = {
        'tasks' : tasks,
        'compltd_tasks':compltd_tasks,
    }
    # return HttpResponse("<h1>Homepage</h1>")
    return render(request, 'home.html', context)