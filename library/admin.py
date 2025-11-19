from django.contrib import admin

from library.models import News, Documents, EventScenarios, WorkPlan, CalendarSignificantDates, Competitions, \
    RegulatoryDocuments, ProfessionalPublications, HistoryLibrarianship, Certification, MethodicalRecommendations


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link_to_doc", "created_at", "updated_ut")
    list_filter = ("title",)


@admin.register(EventScenarios)
class EventScenariosAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(WorkPlan)
class WorkPlanAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(CalendarSignificantDates)
class CalendarSignificantDatesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(Competitions)
class CompetitionsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(RegulatoryDocuments)
class CompetitionsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(ProfessionalPublications)
class ProfessionalPublicationsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(HistoryLibrarianship)
class HistoryLibrarianshipAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)


@admin.register(MethodicalRecommendations)
class MethodicalRecommendationsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "link_url", "created_at", "updated_ut", "owner")
    list_filter = ("title",)
