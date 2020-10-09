from todolist_tally.apps.account.models import User
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from todolist_tally.apps.expense.serializers import UserSerializer, ExpenseSerializer
from todolist_tally.apps.expense.models import Expense


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


