from django.urls import path

from library.apps import LibraryConfig
from library.views import ListNews, ListDocument, ListMethodical, ListEventScenarios, ListWorkPlan, \
    ListCalendarSignificantDates, ListCompetitions, ListRegulatoryDocuments, ListProfessionalPublications, \
    ListHistoryLibrarianship, ListCertification, CreateNews, DetailNews

app_name = LibraryConfig.name

urlpatterns = [
    path("", ListNews.as_view(), name="news"),
    path("documents/", ListDocument.as_view(), name="documents"),
    path("methodical/", ListMethodical.as_view(), name="methodical"),
    path("events/", ListEventScenarios.as_view(), name="events"),
    path("workplans/", ListWorkPlan.as_view(), name="workplans"),
    path("calendary/", ListCalendarSignificantDates.as_view(), name="calendary"),
    path("competitions/", ListCompetitions.as_view(), name="competitions"),
    path("regulatory_documents/", ListRegulatoryDocuments.as_view(), name="regulatory_documents"),
    path("professional_publications/", ListProfessionalPublications.as_view(), name="professional_publications"),
    path("history/", ListHistoryLibrarianship.as_view(), name="history"),
    path("certification/", ListCertification.as_view(), name="certification"),
    path("create_news/", CreateNews.as_view(), name="create_news"),
    path("detail_news/<int:pk>/", DetailNews.as_view(), name="detail_news"),
]
