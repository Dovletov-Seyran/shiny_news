from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, detail, category_news, all_news, about

urlpatterns = [
    path('home/', home, name='home'),
    path('detail/<str:slug>/', detail, name='detail'),
    path('category_news/<str:slug>/', category_news, name='category_news'),
    path('all_news/', all_news, name='all_news'),
    path('about/', about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)