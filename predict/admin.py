from django.contrib import admin

from .models import Relationship, MaleName, FemaleName

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ['male_name', 'female_name']

@admin.register(MaleName)
class MaleNameAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(FemaleName)
class FemaleNameAdmin(admin.ModelAdmin):
    list_display = ['name']
