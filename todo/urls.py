from django.urls import path

from todo.views import TaskListView, TagListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagCreateView, \
    TagUpdateView, TagDeleteView, UndoTaskView, CompleteTaskView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/add", TaskCreateView.as_view(), name="task-add"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/<int:pk>/undo", UndoTaskView.as_view(), name="task-undo"),
    path("tag/<int:pk>/complete", CompleteTaskView.as_view(), name="task-complete"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tag/add", TagCreateView.as_view(), name="tag-add"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
