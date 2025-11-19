from django.shortcuts import render
from django.views.generic import ListView

from library.models import News, Documents, MethodicalRecommendations, EventScenarios


class ListNews(ListView):
    model = News
    template_name = "library/news.html"
    context_object_name = "news"


class ListDocument(ListView):
    model = Documents
    template_name = "library/documents.html"
    context_object_name = "documents"


class ListMethodical(ListView):
    model = MethodicalRecommendations
    template_name = "library/methodical.html"
    context_object_name = "methodical"


class ListEventScenarios(ListView):
    model = EventScenarios
    template_name = "library/events.html"
    context_object_name = "events"