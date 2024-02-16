# projects/admin.py
from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'link')  # Customize the fields displayed in the list view
    search_fields = ('title', 'owner__username')  # Add fields for searching

    # Add any additional customizations as needed

admin.site.register(Project, ProjectAdmin)
