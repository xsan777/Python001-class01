from .models import Qipaoshui
from django.db.models import Avg
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .form import LoginForm
from django.contrib.auth import authenticate,login
# result.html
# from .models import UserProfile
from .models import MyBackend

# def tables_url(requset):
#     return render(requset,'tables.html')

def login_url(request):
    if request.method == 'POST':
        print('-'*50)
        login_form = LoginForm(request.POST)
        print(login_form)
        # 在这里犯过 .is_valid 没括号的错误，发现发起get请求的时候就报了post里的这个问题的错误
        if login_form.is_valid():
            cd = login_form.cleaned_data
            print(cd)
            # 读取表单的返回值
            user = authenticate(email=cd['email'], password=cd['password'])
            # print(type(user))
            if user:
                print('+'*50)
                login(request, user)
                print('='*50)
                return render(request, 'index.html')
            else:
                return render(request, 'login1.html',{'form':login_form})
                # return render(request, 'login1.html')
    if request.method == "GET":
        print('~'*50)
        # email = request.GET.get('email')
        # password = request.GET.get('password')
        # print(email)
        # print(password)
        # user = authenticate(email=email, password=password)
        # if user:
        #     login(request, user)
        #     print("1"*60)
        #     return render(request, 'index.html')
        # else:
        #     print('+'*50)
        #     return render(request, 'login.html')

        login_form = LoginForm()
        return render(request, 'login1.html',{'form':login_form})

def estimate_url(requset,result):
    shorts = Qipaoshui.objects.all()
    # 评论数量
    counter = Qipaoshui.objects.all().count()
    # star_values = Qipaoshui.objects.values_list('n_star')
    # 平均星级
    star_avg = f" {Qipaoshui.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg = f" {Qipaoshui.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
    # 正向数量
    queryset = Qipaoshui.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()
    # 负向数量
    queryset = Qipaoshui.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()
    return render(requset,'result.html',locals())

def index_url(request,index):
    print("1"*60)
    return render(request, 'index.html')

