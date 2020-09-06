from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .loginform import LoginForm


def loginpage(request):
    logininfo = LoginForm()
    return render(request, 'login.html', {'form': logininfo})


def logindo(request):
    if request.method == 'POST':
        logininfo = LoginForm(request.POST)
        if logininfo.is_valid():
            userinfo = logininfo.cleaned_data
            usersucc = authenticate(username=userinfo['username'],
                                    password=userinfo['password'])
            if usersucc:
                login(request, usersucc)
                messages.success(request, '登录成功!')
                return redirect('/index')
            else:
                messages.error(request, '用户密码错误!')
                return redirect('/login')


@login_required
def indexpage(request):
    return HttpResponse('hello world！')