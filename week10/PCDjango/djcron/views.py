from django.shortcuts import render

# Create your views here.
from .models import Phone, PhoneCPages, PhoneCDetails
from django.db.models import Avg

def phone_comments(request):
    ###  从models取数据传给template  ###
    comments = PhoneCDetails.objects.all()
    # 评论数量
    counter = PhoneCDetails.objects.all().count()

    # 情感倾向
    sent_avg =f" {PhoneCDetails.objects.aggregate(Avg('comment_sentiments'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = PhoneCDetails.objects.values('comment_sentiments')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = PhoneCDetails.objects.values('comment_sentiments')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()


    return render(request, 'result.html', locals())