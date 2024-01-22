from django.shortcuts import render

from .models import Category, News
from helpers.shortcuts import get_object_from_qs_or_404


def home(request):
    four_categories = Category.objects.all()[0:4]
    context = {'four_categories': four_categories}
    return render(request, 'home.html', context)

def detail(request, slug):
    qs = News.objects.all()
    news = get_object_from_qs_or_404(qs, slug=slug)
    context = {
        "news": news
    }
    return render(request, 'detail.html', context)

def category_news(request, slug):
    qs = Category.objects.all()
    category = get_object_from_qs_or_404(qs, slug=slug)
    all_news = category.news.all()
    context = {
        "category": category,
        "all_news": all_news
    }
    return render(request, 'category-news.html', context)

def all_news(request):
    twenty_news = News.objects.all()[0:21]
    context = {'twenty_news': twenty_news}
    return render(request, 'all-news.html', context)

def about(request):
    return render(request, 'about.html')



