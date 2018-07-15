from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.


def index(request):
    A = [1, 3, 6, 4, 1, 2]
    rel = len(A) + 1
    for i in range(1, len(A) + 1):
        if i not in A:
            rel = i
            break
    print(rel)

    news = News.objects.all()
    return render(request, 'twodays/index.html', {'news': news})
