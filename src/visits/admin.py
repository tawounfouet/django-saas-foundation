from django.contrib import admin
from .models import PageVisit  # Import your PageVisit model

# Register the PageVisit model with Django admin
@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('path', 'timestamp')  # Show these fields in the admin list view
    search_fields = ('path',)  # Allow searching by the path field
    list_filter = ('timestamp',)  # Add a filter for the timestamp field

# You can customize list_display, search_fields, and list_filter to fit your needs
