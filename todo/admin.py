from django.contrib import admin
from .models import Task

# to edit the ADMIN PAGE so that some internal details are also seen on the main screen
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at') # changes the look of the database table
    # use the variable name = list_display
    
    search_fields = ('task',)
    # use the same variable name!!

# Register your models here.
admin.site.register(Task, TaskAdmin)