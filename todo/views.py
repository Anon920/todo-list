from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"
    ordering = ['done', '-created_at']


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = ""
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = ""
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = ""
    success_url = reverse_lazy("todo:home")


class TagListView(ListView):
    model = Tag
    template_name = "tags.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tag_add.html"
    success_url = reverse_lazy("todo:tags")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = ""
    success_url = reverse_lazy("todo:tags")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = ""
    success_url = reverse_lazy("todo:tags")


class CompleteTaskView(View):
    def post(self, pk, request):
        task = get_object_or_404(Task, pk=pk)
        task.done = True
        task.save()
        return redirect("todo:home")


class UndoTaskView(View):
    def post(self, pk, request):
        task = get_object_or_404(Task, pk=pk)
        task.done = False
        task.save()
        return redirect("todo:home")
