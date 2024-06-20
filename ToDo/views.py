from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .forms import TaskForm
from .models import Task


@method_decorator(never_cache, name='dispatch')
class TaskListView(LoginRequiredMixin, View):
    login_url = 'UserAuth/login/'  

    def get(self, request):
        tasks = Task.objects.all()
        form = TaskForm()
        return render(request, 'task_list.html', {'tasks': tasks, 'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task-list')


@method_decorator(never_cache, name='dispatch')
class TaskUpdateView(LoginRequiredMixin, View):
    login_url = 'UserAuth/login/'  

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'task_form.html', {'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('task-list')


@method_decorator(never_cache, name='dispatch')
class TaskDeleteView(LoginRequiredMixin, View):
    login_url = 'UserAuth/login/'  

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task-list')


@method_decorator(never_cache, name='dispatch')
class TaskToggleStatusView(LoginRequiredMixin, View):
    login_url = 'UserAuth/login/'  

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.status = 'completed' if task.status == 'pending' else 'pending'
        task.save()
        return redirect('task-list')
