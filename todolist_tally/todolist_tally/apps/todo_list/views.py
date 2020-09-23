from django.shortcuts import render
# Create your views here.
from todolist_tally.apps.todo_list.form import TodoForm
from todolist_tally.apps.todo_list.models import Todo
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import response


def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        one_todo = Todo(content=content)
        one_todo.save()
    todo_list = list(Todo.objects.all())
    form = TodoForm()
    context_dict = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo_list/index.html', context_dict)


class Edit_todo(View):
    form_class = TodoForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return response(status=200)
        return response(status=500)



class Finish_todo(View):

    def get(self, request, id):
        print("hello world!")

    def post(self, request):
        return 'oooo'
