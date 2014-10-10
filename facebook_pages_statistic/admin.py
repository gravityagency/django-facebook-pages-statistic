# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import PageStatistic


class PageStatisticAdmin(admin.ModelAdmin):
    search_fields = ("page",)
    list_display = ("page", "likes", "shares", "parse_date",)


admin.site.register(PageStatistic, PageStatisticAdmin)