import urllib.parse
from .models import Shouji
from django.db.models import Avg
from django.shortcuts import render,redirect
from .form import RequestForm

# Create your views here.

def estimate_url(request):
    form = RequestForm()
    shorts = Shouji.objects.all()
    # 评论数量
    counter = Shouji.objects.all().count()
    # 平均星级
    star_avg = f" {Shouji.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg = f" {Shouji.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
    # 正向数量
    queryset = Shouji.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()
    # 负向数量
    queryset = Shouji.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()
    return render(request,'result1.html',locals())

# action="/request_url" method="post"
def request_url(request,name):
    if request.method == 'POST':
        try:
            condtions = {}
            form = RequestForm(request.POST)
            # print('+'*70)
            # print(form)
            if form.is_valid():
                cd = form.cleaned_data
                if cd['text']:
                    # print('-'*40)
                    cd['text']= urllib.parse.unquote(cd['text'])
                    # print(cd['text'])
                    condtions['estimate__contains'] = cd['text']
                if cd['start_time']:
                    # print('='*40)
                    # print(cd['start_time'])
                    condtions['date__gte'] = cd['start_time']
                if cd['last_time']:
                    # print(cd['last_time'])
                    condtions['date__lte'] = cd['last_time']
                shorts = Shouji.objects.filter(**condtions)
                counter = Shouji.objects.filter(**condtions).count()
                # 平均星级
                star_avg = f"{Shouji.objects.filter(**condtions).aggregate(Avg('n_star'))['n_star__avg']:0.1f}"
                # 情感倾向
                sent_avg = f"{Shouji.objects.filter(**condtions).aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"
                # 正向数量
                queryset = Shouji.objects.filter(**condtions).values('sentiment')
                condtions = {'sentiment__gte': 0.5}
                plus = queryset.filter(**condtions).count()
                # 负向数量
                queryset = Shouji.objects.filter(**condtions).values('sentiment')
                condtions = {'sentiment__lt': 0.5}
                minus = queryset.filter(**condtions).count()
                return render(request, 'result1.html',locals())
        except Exception:
            form = RequestForm()
            point = '没有您搜索的信息...'
            return render(request, 'result1.html',locals())
    if request.method == "GET":
        form = RequestForm()
        # text = request.GET.get('text')
        # start_time = request.GET.get('start_time')
        # last_time = request.GET.get('last_time')
        # condtions = {}
        # if text:
        #     print(text)
        #     condtions['estimate__contains'] = text
        # if start_time:
        #     print(start_time)
        #     condtions['date__gte'] = start_time
        # if last_time:
        #     print(last_time)
        #     condtions['date__lte'] = last_time
        # shorts = Shouji.objects.filter(**condtions)
        # counter = Shouji.objects.filter(**condtions).count()
        #  # 平均星级
        # star_avg = f"{Shouji.objects.filter(**condtions).aggregate(Avg('n_star'))['n_star__avg']:0.1f}"
        # # 情感倾向
        # sent_avg = f"{Shouji.objects.filter(**condtions).aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"
        # # 正向数量
        # queryset = Shouji.objects.filter(**condtions).values('sentiment')
        # condtions = {'sentiment__gte': 0.5}
        # plus = queryset.filter(**condtions).count()
        # # 负向数量
        # queryset = Shouji.objects.filter(**condtions).values('sentiment')
        # condtions = {'sentiment__lt': 0.5}
        # minus = queryset.filter(**condtions).count()
        # print('~'*40)
        return render(request, 'result1.html',locals())

    # 'lt,lte,gt,gte,contains,icontains'