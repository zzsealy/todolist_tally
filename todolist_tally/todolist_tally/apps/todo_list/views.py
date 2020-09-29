from django.shortcuts import render
# Create your views here.
from todolist_tally.apps.todo_list.models import Todo
# from django.views.generic import View
# from django.contrib.auth.decorators import login_required
from django.http import response, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
from todolist_tally.apps.todo_list.utils import format_time
from todolist_tally.apps.account.utils import my_decorator

@my_decorator
def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        prepare_finish_time = request.POST.get('time')
        one_todo = Todo(content=content, prepare_finish_time=prepare_finish_time)
        one_todo.save()
    todo_list = Todo.objects.all()
    context_dict = {'todo_list': todo_list}
    return render(request, 'todo_list/index.html', context_dict)

@csrf_exempt
def edit_todo(request):
    if request.method == 'PUT':
        body = json.loads(request.body)
        id = body['id']
        content = body['content']
        todo = Todo.objects.get(id = id)
        todo.content = content
        todo.save()
        msg = "修改成功"
        return JsonResponse(data={'msg':msg})

@csrf_exempt
def toggle_todo(request, **kwargs):
    if request.method == 'POST':
        body = json.loads(request.body)
        today = time.strftime("%Y-%m-%d", time.localtime())  # 格式化用的
        id = body['id']
        todo = Todo.objects.get(id = id)
        todo.done = not todo.done # 取反
        todo.finished_time = today
        todo.save()
        today = format_time(today)
        prepare_finish_date = format_time(todo.prepare_finish_time)
        if today > prepare_finish_date:
            msg = "逾期完成！"
        else:
            msg = "按时完成"
        if todo.done is False:
            msg = "你取消了"
        return JsonResponse(data={'msg':msg})


