from django.contrib import admin
from .models import *

@admin.register(URLShortener)
class URLShortenerAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'created_at','no_of_count')
    list_filter = ('created_at',)
    search_fields = ('long_url', 'short_url')

