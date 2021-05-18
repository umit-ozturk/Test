from django.contrib import admin

from stringfinder.models import Text


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "text",
    ]
    search_fields = [
        "text",
    ]

