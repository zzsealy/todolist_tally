from todolist_tally.apps.account.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers
from todolist_tally.apps.expense.models import Expense

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        fields = ['user', 'category', 'money']