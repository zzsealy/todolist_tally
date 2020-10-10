from todolist_tally.apps.account.models import User
from django.contrib.auth.models import Group
from rest_framework import serializers
from todolist_tally.apps.expense.models import Expense

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url', 'email']


class ExpenseSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    user_link = UserSerializer().fields['url']
    # days_since_joined = serializers.SerializerMethodField()
    #
    # # 方法写法：get_ + 字段
    # def get_days_since_joined(self, obj):
    #     # obj指这个model的对象
    #     return (now() - obj.date_joined).days

    # post 重写update
    # def create(self, validated_data):
    #     # 除了用户，其他数据可以从validated_data这个字典中获取
    #     # 注意，users在这里是放在上下文中的request，而不是直接的request
    #     user = self.context['request'].user
    #     name = validated_data['name ']
    #     content = validated_data['content ']
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     # 更新的特别之处在于你已经获取到了这个对象instance
    #     instance.name = validated_data.get('name')
    #     instance.content = validated_data.get('content')
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        print(validated_data)

    class Meta:
        model = Expense
        fields = ['user_name','user_link', 'category', 'money']