from django.shortcuts import render
# Create your views here.
from todolist_tally.apps.todo_list.models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
from .utils import format_time
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from todolist_tally.apps.account.models import User
from todolist_tally.settings import PER_PAGE
from django.core.paginator import Paginator


@login_required()
def index(request, page=None):
    user = request.user
    todo_list = Todo.objects.filter(user=user)
    if request.method == 'POST':
        content = request.POST.get('content')
        prepare_finish_time = request.POST.get('time')
        if content and prepare_finish_time:
            one_todo = Todo(user=user,
                            content=content,
                            prepare_finish_time=prepare_finish_time)
            one_todo.save()
    paginator = Paginator(todo_list, PER_PAGE)
    pages_list = [x + 1 for x in range(paginator.num_pages)]
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dict = {'todo_list': page_obj, "username": user, "pages_list": pages_list}
    return render(request, 'todo_list/index.html', context_dict)


def index_filter(request, username, value):
    ll = User.objects.get(username="ll")
    drq = User.objects.get(username="drq")
    user = User.objects.get(username=username)
    if value == "all":
        todo_list = Todo.objects.filter(Q(user=drq) | Q(user=ll))
    elif value == "ll":
        todo_list = Todo.objects.filter(user=ll)
    elif value == "drq":
        todo_list = Todo.objects.filter(user=drq)
    elif value == 'done':
        todo_list = Todo.objects.filter(Q(done=True), Q(user=user))
    elif value == 'notdone':
        todo_list = Todo.objects.filter(Q(done=False), Q(user=user))
    paginator = Paginator(todo_list, PER_PAGE)
    pages_list = [x + 1 for x in range(paginator.num_pages)]
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dict = {'todo_list': page_obj, "username": user, "pages_list": pages_list}
    return render(request, 'todo_list/filter.html', context_dict)


@csrf_exempt
def edit_todo(request):
    if request.method == 'PUT':
        body = json.loads(request.body)
        id = body['id']
        content = body['content']
        todo = Todo.objects.get(id=id)
        todo.content = content
        todo.save()
        msg = "修改成功"
        return JsonResponse(data={'msg': msg})


@csrf_exempt
def toggle_todo(request, **kwargs):
    if request.method == 'POST':
        body = json.loads(request.body)
        today = time.strftime("%Y-%m-%d", time.localtime())  # 格式化用的
        id = body['id']
        todo = Todo.objects.get(id=id)
        todo.done = not todo.done  # 取反
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
        return JsonResponse(data={'msg': msg})


@csrf_exempt
def del_todo(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        id = body['id']
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse(data={'msg': "删除成功"})
