from django.contrib import admin

from .models import Relationship

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ['male_name', 'female_name']
