from django.urls import path
from todolist_tally.apps.todo_list import views

urlpatterns = [
    # 登陆url
    path('', views.index),
    path('edit-todo', views.Edit_todo.as_view(), name='edit_todo'),
    path('toggle-todo', views.toggle_todo, name='toggle_todo')
]