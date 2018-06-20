from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.
def index(request):
	news = News.objects.all()
	return render(request, 'twodays/index.html', {'news': news})