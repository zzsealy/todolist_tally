from django.urls import path
from todolist_tally.apps.todo_list import views

urlpatterns = [
    # 登陆url
    path('', views.index, name='index'),
    path('toggle-todo', views.toggle_todo, name='toggle_todo'),
    path('edit-todo', views.edit_todo, name='edit_todo'),
    path('del-todo', views.del_todo, name='del_todo'),
    path('index-filter/<str:username>/<str:value>', views.index_filter, name="index_filter"),
]
