from django.urls import path
from rest_framework import routers

from library.apps import LibraryConfig
from library.views import ListNews, ListDocument, ListMethodical, ListEventScenarios, ListWorkPlan, \
    ListCalendarSignificantDates, ListCompetitions, ListRegulatoryDocuments, ListProfessionalPublications, \
    ListHistoryLibrarianship, ListCertification, CreateNews, DetailNews, NewsViewSet, DocumentsViewSet, \
    EventScenariosViewSet, WorkPlanViewSet, CalendarSignificantDatesViewSet, CompetitionsViewSet, \
    RegulatoryDocumentsViewSet, ProfessionalPublicationsViewSet, HistoryLibrarianshipViewSet, CertificationViewSet, \
    MethodicalRecommendationsViewSet

app_name = LibraryConfig.name

router = routers.DefaultRouter()
router.register(r"api/news", NewsViewSet, basename="news")
router.register(r"api/documents", DocumentsViewSet, basename="documents")
router.register(r"api/event_scenarios", EventScenariosViewSet, basename="event_scenarios")
router.register(r"api/work_plan", WorkPlanViewSet, basename="work_plan")
router.register(r"api/calendar_significant_dates", CalendarSignificantDatesViewSet, basename="calendar_significant_dates")
router.register(r"api/competitions", CompetitionsViewSet, basename="competitions")
router.register(r"api/regulatory_documents", RegulatoryDocumentsViewSet, basename="regulatory_documents")
router.register(r"api/professional_publications", ProfessionalPublicationsViewSet, basename="professional_publications")
router.register(r"api/history_librarianship", HistoryLibrarianshipViewSet, basename="history_librarianship")
router.register(r"api/certification", CertificationViewSet, basename="certification")
router.register(r"api/methodical_recommendations", MethodicalRecommendationsViewSet, basename="methodical_recommendations")


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
] + router.urls
