from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.

    # from this function we put the data that we get from the form in home.html to forward to database
    # FORM WITH 'POST' METHOD
def addTask(request):

    task = request.POST['task'] # INPUT FIELD'S name='task' ATTRIBUTE

    #to input to database
    Task.objects.create(task=task)

    #return HttpResponse("<h2>The form is submitted</h2>")
    # rather than returning this response we refresh the page so that it is seen as a task
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk = pk)

    #Task.objects.update(task=task, is_completed=True)
    task.is_completed = True
    task.save()

    # return HttpResponse(task)
    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk = pk)

    task.is_completed = False
    task.save()

    return redirect('home')
    

def edit_task(request, pk): 
    task = get_object_or_404(Task, pk=pk)

    # here we have two kinds of requests
    # GET = when we just want to retrieve the name of the task
    # POST = when update button is pressed and we want to write to the database
    if request.method == 'POST':
        task.task = request.POST['task']
        task.save()

        return redirect('home')
    else:
        context = {
            'task' : task,
        }
    
    return render(request, 'edit_task.html', context)



def delete_task(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete() # deletes that particular task object
    return redirect('home')
