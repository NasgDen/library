from django.shortcuts import render
from django.views.generic import ListView

from library.models import News


class ListNews(ListView):
    model = News
    template_name = "library/news.html"
    context_object_name = "news"
