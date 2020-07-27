from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from User.models import UserInformation
from .models import Task, Event
from .forms import TaskForm


def create_event(task_id, user_id, event_type):

    user = User.objects.get(pk=user_id)
    task = Task.objects.get(pk=task_id)

    event = Event(
        user=user,
        task=task
    )
    event.event_type = event_type
    event.save()


def my_tasks(request):
    try:
        if not request.session["logged_in"]:
            messages.warning(request, 'Kindly login before accessing the service.')  
            return redirect('login')
    except:
        messages.warning(request, 'Kindly login before accessing the service.')
        return redirect('login')

    user_id = request.session['id']
    user = User.objects.get(pk=user_id)
    
    tasks = Task.objects.filter(user=user, deleted=False)
    task_data = []

    for task in tasks:
        task_information = {
            "name": task.name,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "date_added": task.date_added,
            "date_updated": task.date_updated,
            "edit_url": f"/task/edit-task/{task.pk}",
            "delete_url": f"/task/delete-task/{task.pk}"
        }

        task_data.append(task_information)

    data = {
        "title": "Task Dashboard",
        "tasks": task_data
    }

    return render(request, 'Task/my_tasks.html', data)


def add_task(request):
    try:
        if not request.session["logged_in"]:
            messages.warning(request, 'Kindly login before accessing the service.')  
            return redirect('login')
    except:
        messages.warning(request, 'Kindly login before accessing the service.')
        return redirect('login')

    user_id = request.session['id']
    user = User.objects.get(pk=user_id)

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = Task()
            task.user = user
            task.name = form.cleaned_data.get('name')
            task.description = form.cleaned_data.get('description')
            task.priority = form.cleaned_data.get('priority')
            task.status = form.cleaned_data.get('status')
            task.save()

            create_event(task.pk, user_id, 'Creation')

            messages.success(request, 'Task successfully created.')
            return redirect('my-tasks')
        else:
            messages.warning(request, form.errors)
            return redirect('add-task')
    else:
        form = TaskForm()

    data = {
        "form": form,
        "title": "Add Task"
    }

    return render(request, 'Task/add_task.html', data)


def edit_task(request, task_id):
    try:
        if not request.session["logged_in"]:
            messages.warning(request, 'Kindly login before accessing the service.')  
            return redirect('login')
    except:
        messages.warning(request, 'Kindly login before accessing the service.')
        return redirect('login')

    task = Task.objects.get(pk=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task.name = form.cleaned_data.get('name')
            task.description = form.cleaned_data.get('description')
            task.priority = form.cleaned_data.get('priority')
            task.status = form.cleaned_data.get('status')
            task.save()

            create_event(task.pk, task.user.pk, 'Updation')

            messages.success(request, 'Task successfully edited.')
            return redirect('my-tasks')
        else:
            messages.warning(request, form.errors)
            return redirect('edit-task')
    else:
        form = TaskForm(initial={"name": task.name,"description": task.description,"priority": task.priority,"status": task.status})

    data = {
        "form": form,
        "title": "Edit Task"
    }

    return render(request, 'Task/add_task.html', data)


def delete_task(request, task_id):
    try:
        if not request.session["logged_in"]:
            messages.warning(request, 'Kindly login before accessing the service.')  
            return redirect('login')
    except:
        messages.warning(request, 'Kindly login before accessing the service.')
        return redirect('login')

    task = Task.objects.get(pk=task_id)
    task.deleted = True
    task.save()

    create_event(task.pk, task.user.pk, 'Deletion')

    messages.success(request, 'Task successfully deleted.')
    return redirect('my-tasks')


def task_track(request):
    try:
        if not request.session["logged_in"]:
            messages.warning(request, 'Kindly login before accessing the service.')  
            return redirect('login')
    except:
        messages.warning(request, 'Kindly login before accessing the service.')
        return redirect('login')

    user_id = request.session['id']
    user = User.objects.get(pk=user_id)

    events = Event.objects.filter(user=user).order_by('-time_of_event')
    event_data = []

    for event in events:
        event_information = {
            "task_name": event.task.name,
            "event_type": event.event_type,
            "time_of_event": event.time_of_event,
        }

        event_data.append(event_information)

    data = {
        "title": "Task Tracker",
        "events": event_data
    }

    return render(request, 'Task/task_track.html', data)