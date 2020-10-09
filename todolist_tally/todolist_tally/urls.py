"""todolist_tally URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todolist_tally.apps.expense.views import UserViewSet,ExpenseViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view




router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('expenses', ExpenseViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('todolist_tally.apps.todo_list.urls')),
    path('account/', include('todolist_tally.apps.account.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-expense/', include('rest_framework.urls', namespace='rest_framework')),
]

