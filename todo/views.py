from django.shortcuts import render, redirect
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
    
