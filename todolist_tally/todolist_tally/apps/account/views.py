# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from todolist_tally.apps.account.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# 这个是django原生的
from django.contrib.auth import authenticate, logout, login


class LoginView(View):  # 文档里说通用视图自动创建ModelForm,只要他们能找出要是用的模型类
    template_name = "account/login.html"

    # def form_valid(self, form):
    #     # 默认实现了 form_valid()  简单重定向至 success_url 。
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super().form_valid()

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user) # 登录
            return redirect("index")
        else:
            return render(request, self.template_name, {'error': "用户不存在"})
        # if user.check_password(password):
        #
        #     if username not in usernamelist:
        #
        #     return redirect("index")
        return render(request, self.template_name, {'error': "密码不正确"})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if password1 != password2:
            return render(request, 'account/register.html', {'error': "两次输入密码不一致"})
        u = User(username=username, email=email)
        u.set_password(password1)
        u.save()
        return redirect("login")
    return render(request, 'account/register.html')


def user_logout(request):
    logout(request)
    return redirect('login')


class UserDetail(View):
    pass
