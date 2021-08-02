from django.urls import path

from tasks.views import (
    create_task, all_tasks,
    task_detail, task_delete,
    search, complete_task,
    completed_tasks
)

urlpatterns = [
    path('tasks/completed/', completed_tasks, name='completed_tasks'),
    path('task/complete/<int:pk>', complete_task, name='complete_task'),
    path('search', search, name='search'),
    path('create-task/', create_task, name='create_task'),
    path('task/delete/<int:pk>', task_delete, name='task_delete'),
    path('task/<int:pk>', task_detail, name='task_detail'),
    path('', all_tasks, name='all_tasks'),
]
