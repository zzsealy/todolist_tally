from django.urls import path
from todolist_tally.apps.account import views

urlpatterns = [
    path('<int:id>', views.UserDetail.as_view(), name='user_detail'),
    path('login', views.LoginView.as_view(), name='login')
]