from todolist_tally.apps.account.models import User
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from todolist_tally.apps.expense.serializers import UserSerializer, ExpenseSerializer
from todolist_tally.apps.expense.models import Expense
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

#
# @api_view(['GET', 'POST'])
# def expense_list(request):
#     if request.method == 'GET':
#         expense = Expense.objects.all()
#         serializer = ExpenseSerializer(expense, many=True)
#         return Response(serializer.data)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    for ex in queryset:
       ex['username'] = ex.user.username

    serializer_class = ExpenseSerializer


