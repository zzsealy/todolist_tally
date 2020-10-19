from django.shortcuts import render


# def my_decorator(func):
#     def warpper(request, *args, **kwargs):
#         usernamelist = ['drq', 'liuli', 'xiaoguaishou', 'dairuiquan']
#         if request.user.username not in usernamelist:
#             return render(request, 'account/404.html')
#         return func(request, *args, **kwargs)
#     return warpper
