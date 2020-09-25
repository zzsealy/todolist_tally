from django.urls import path
from todolist_tally.apps.todo_list import views

urlpatterns = [
    # 登陆url
    path('', views.index),
    path('toggle-todo', views.toggle_todo, name='toggle_todo')
]