from django.urls import path
from . import views

urlpatterns = [
    # add a task
    path('addtask/', views.addTask, name = 'addTask'),

    # mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name = 'mark_as_done'),
    # because every database object has a unique primary key

    # mark as undone
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name= 'mark_as_undone'),

    # delete task
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),

    # edit a task
    path('edit_task/<int:pk>', views.edit_task, name="edit_task")
]