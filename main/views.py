from django.shortcuts import render
from .models import Category, News

def home(request):
    four_categories = Category.objects.all()[0:4]
    context = {'four_categories': four_categories}
    return render(request, 'home.html', context)

def detail(request):
    return render(request, 'detail.html')

def category_news(request):
    return render(request, 'category-news.html')

def all_news(request):
    twenty_news = News.objects.all()[0:21]
    context = {'twenty_news': twenty_news}
    return render(request, 'all-news.html', context)

def about(request):
    return render(request, 'about.html')



