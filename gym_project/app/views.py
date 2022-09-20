from django.shortcuts import render, redirect

# Create your views here.
from app import models
from app.forms import TaskForm
from app.models import Task


def home(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'login.html')


def admin_panel(request):
    return render(request, 'admin_home.html')


def card(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    return render(request, 'card.html', {'form': form})


def card_view(request):
    data = Task.objects.all()
    return render(request, 'card_view.html', {'data': data})


def card_update(request, id):
    data = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('card_view')
    else:
        form = TaskForm(instance=data)
    return render(request, 'card_update.html', {'form': form})


def card_delete(request, id):
    data = Task.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('card_view')
    else:
        return redirect('card_view')
