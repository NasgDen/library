from django.urls import path

from library.apps import LibraryConfig
from library.views import ListNews, ListDocument, ListMethodical, ListEventScenarios, ListWorkPlan

app_name = LibraryConfig.name

urlpatterns = [
    path("", ListNews.as_view(), name="news"),
    path("documents/", ListDocument.as_view(), name="documents"),
    path("methodical/", ListMethodical.as_view(), name="methodical"),
    path("events/", ListEventScenarios.as_view(), name="events"),
    path("workplans/", ListWorkPlan.as_view(), name="workplans"),
]
