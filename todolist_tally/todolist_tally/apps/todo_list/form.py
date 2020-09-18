from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(label="标题")
    content = forms.CharField(label='内容')
    prepare_finish_time = forms.DateTimeField(label="预计完成时间")
    finished_time = forms.DateTimeField(label="完成时间")


