from django.shortcuts import render
# Create your views here.
from todolist_tally.apps.todo_list.form import TodoForm
from todolist_tally.apps.todo_list.models import Todo
import datetime
from django.views.generic import View

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        prepare_finish_time = request.POST.get('prepare_finish_time')
        prepare_finish_time = datetime.datetime.strptime(prepare_finish_time, '%Y-%m-%d')
        one_todo = Todo(title=title, content=content, prepare_finish_time=prepare_finish_time)
        one_todo.save()
    todo_list = list(Todo.objects.all())
    form = TodoForm()
    context_dict = {'todo_list': todo_list, 'form':form}
    return render(request, 'todo_list/index.html', context_dict)


class Finish_todo(View):

    def get(self,request, id):
        print("hello world!")

    def post(self, request):
        return 'oooo'
