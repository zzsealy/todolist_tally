from django.shortcuts import render
# Create your views here.
from todolist_tally.apps.todo_list.form import TodoForm
from todolist_tally.apps.todo_list.models import Todo
from django.views.generic import View
from django.http import response, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        one_todo = Todo(content=content)
        one_todo.save()
    todo_list = Todo.objects.all()
    context_dict = {'todo_list': todo_list}
    return render(request, 'todo_list/index.html', context_dict)


class Edit_todo(View):
    form_class = TodoForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return response(status=200)
        return response(status=500)


@csrf_exempt
def toggle_todo(request, **kwargs):
    if request.method == 'POST':
        body = json.loads(request.body)
        id = body['id']
        todo = Todo.objects.get(id = id)
        todo.done = not todo.done # 取反
        todo.save()
        return JsonResponse(data={'success':'ok'})


