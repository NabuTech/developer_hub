# profiles/admin.py
from django.contrib import admin
from .models import Profile, Skill

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')  # Customize the fields displayed in the list view
    search_fields = ('user__username', 'location')  # Add fields for searching

    # Add any additional customizations as needed

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill)
