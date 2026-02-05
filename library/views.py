from django.core.serializers import serialize
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from rest_framework import viewsets

from library.forms import NewsForm
from library.models import News, Documents, MethodicalRecommendations, EventScenarios, WorkPlan, \
    CalendarSignificantDates, Competitions, RegulatoryDocuments, ProfessionalPublications, HistoryLibrarianship, \
    Certification
from library.serializers import NewsSerializer, DocumentsSerializer, EventScenariosSerializer, WorkPlanSerializer, \
    CalendarSignificantDatesSerializer, CompetitionsSerializer, RegulatoryDocumentsSerializer, \
    ProfessionalPublicationsSerializer, HistoryLibrarianshipSerializer, CertificationSerializer, \
    MethodicalRecommendationsSerializer


class ListNews(ListView):
    model = News
    template_name = "library/news.html"
    context_object_name = "news"


class CreateNews(CreateView):
    model = News
    form_class = NewsForm
    # fields = ['title', 'content',]
    template_name = "library/create_news.html"
    success_url = reverse_lazy("library:news")
    context_object_name = "news"


class DetailNews(DetailView):
    model = News
    template_name = "library/detail_news.html"
    context_object_name = 'news'


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


class ListWorkPlan(ListView):
    """ Отображает - План работ """

    model = WorkPlan
    template_name = "library/workplans.html"
    context_object_name = "workplans"


class ListCalendarSignificantDates(ListView):
    """ Отображает - календарь знаменательных дат """

    model = CalendarSignificantDates
    template_name = "library/calendary.html"
    context_object_name = "calendars"


class ListCompetitions(ListView):
    """ Отображает - Конкурсы """

    model = Competitions
    template_name = "library/competitions.html"
    context_object_name = "competitions"


class ListRegulatoryDocuments(ListView):
    """ Отображает - Нормативные документы """

    model = RegulatoryDocuments
    template_name = "library/regulatory_documents.html"
    context_object_name = "documents"


class ListProfessionalPublications(ListView):
    """ Отображает - Профессиональные издания """

    model = ProfessionalPublications
    template_name = "library/professional_publications.html"
    context_object_name = "publications"


class ListHistoryLibrarianship(ListView):
    """ Отображает - Историю библиотечного дела """

    model = HistoryLibrarianship
    template_name = "library/history.html"
    context_object_name = "histories"


class ListCertification(ListView):
    """  Отображает - Аттестацию """

    model = Certification
    template_name = "library/certification.html"
    context_object_name = "certifications"

    # DRF


class NewsViewSet(viewsets.ModelViewSet):
    """ ViewSet для модули News """

    queryset = News.objects.all()
    serializer_class = NewsSerializer


class DocumentsViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели Documents """

    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class EventScenariosViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели EventScenarios """

    queryset = EventScenarios.objects.all()
    serializer_class = EventScenariosSerializer


class WorkPlanViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели WorkPlan """

    queryset = WorkPlan.objects.all()
    serializer_class = WorkPlanSerializer


class CalendarSignificantDatesViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели CalendarSignificantDates """

    queryset = CalendarSignificantDates.objects.all()
    serializer_class = CalendarSignificantDatesSerializer


class CompetitionsViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели Competitions """

    queryset = Competitions.objects.all()
    serializer_class = CompetitionsSerializer


class RegulatoryDocumentsViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели RegulatoryDocuments """

    queryset = RegulatoryDocuments.objects.all()
    serializer_class = RegulatoryDocumentsSerializer


class ProfessionalPublicationsViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели ProfessionalPublications """

    queryset = ProfessionalPublications.objects.all()
    serializer_class = ProfessionalPublicationsSerializer


class HistoryLibrarianshipViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели HistoryLibrarianship """

    queryset = HistoryLibrarianship.objects.all()
    serializer_class = HistoryLibrarianshipSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели Certification """

    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class MethodicalRecommendationsViewSet(viewsets.ModelViewSet):
    """ ViewsSet для модели MethodicalRecommendations """

    queryset = MethodicalRecommendations.objects.all()
    serializer_class = MethodicalRecommendationsSerializer