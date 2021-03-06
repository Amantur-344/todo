from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

            # cd = form.cleaned_data
            # title = cd.get('title')
            # description = cd.get('description')
            # deadline = cd.get('deadline')
            # task = Task(title=title,
            #             description=description,
            #             deadline=deadline)
            # task.save()

            # Task.objects.create(
            #     title=title,
            #     description=description,
            #     deadline=deadline
            # )

            # task = Task()
    form = TaskForm()
    print(form)
    return render(request, 'tasks/create_task.html',
                  context={'form': form})


def all_tasks(request):
    tasks = Task.completed.all()
    paginator = Paginator(tasks, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tasks/all_tasks.html',
                  context={'page_obj': page_obj})


def task_detail(request, pk):
    task = Task.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = TaskForm(instance=task)
    return render(request, 'tasks/task_detail.html',
                  context={'form': form})


def task_delete(request, pk):
    task = Task.objects.filter(id=pk).first()
    task.delete()
    return redirect('/')


def search(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(done=False).filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    return render(request, 'tasks/all_tasks.html',
                  context={'tasks': tasks})


def complete_task(request, pk):
    task = Task.objects.filter(id=pk).first()
    task.done = True
    task.save()
    return redirect('/tasks/completed/')


def completed_tasks(request):
    tasks = Task.objects.filter(done=True)
    return render(request, 'tasks/completed_tasks.html',
                  context={'tasks': tasks})


def register():
    pass


def asd():
  pass


def test():
    pass