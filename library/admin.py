from django.contrib import admin

from library.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "created_at",
        "updated_ut"
    )
    list_filter = ("title",)
