from django.shortcuts import render
from django.views.generic import ListView

from library.models import News, Documents, MethodicalRecommendations, EventScenarios, WorkPlan, \
    CalendarSignificantDates, Competitions, RegulatoryDocuments, ProfessionalPublications, HistoryLibrarianship, \
    Certification


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