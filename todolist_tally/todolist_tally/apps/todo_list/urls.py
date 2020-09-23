from django.urls import path
from todolist_tally.apps.todo_list import views

urlpatterns = [
    # 登陆url
    path('', views.index),
    path('finish-<int:id>/', views.Finish_todo.as_view(), name ='finish-todo'),
    path('edit-todo', views.Edit_todo.as_view(), name='edit_todo')
]