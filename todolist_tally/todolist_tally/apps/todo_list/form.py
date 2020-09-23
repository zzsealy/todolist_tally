from django.forms import ModelForm
from todolist_tally.apps.todo_list.models import Todo


class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
