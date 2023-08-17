from django.views.generic import ListView, DetailView

from todo.models import Todo


class TodoList(ListView):
    model = Todo
    context_object_name = 'todoes'
    template_name = 'todo/todo_list.html'


class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo/todo_detail.html'