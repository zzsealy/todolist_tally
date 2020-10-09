from todolist_tally.apps.account.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers
from todolist_tally.apps.expense.models import Expense

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url', 'email']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['user', 'category', 'money']