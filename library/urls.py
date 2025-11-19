from django.urls import path

from library.apps import LibraryConfig
from library.views import ListNews

app_name = LibraryConfig.name

urlpatterns = [
    path("", ListNews.as_view(), name="news"),
]
