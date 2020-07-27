from django.urls import path
from .views import *


urlpatterns = [
    path('my-tasks', my_tasks, name="my-tasks"),
    path('add-task', add_task, name="add-task"),
    path('edit-task/<int:task_id>', edit_task, name="edit-task"),
    path('delete-task/<int:task_id>', delete_task, name="delete-task"),
    path('task-track', task_track, name="tasks-track"),
]
