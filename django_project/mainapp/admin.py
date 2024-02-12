from django.contrib import admin
from django.apps import apps
from .models import *


@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ['user', 'word_ru', 'word_en']
    list_display_links = ['word_ru']


@admin.register(Technic)
class TechnicAdmin(admin.ModelAdmin):
    list_display = ['user', 'word_ru', 'word_en']
    list_display_links = ['word_ru']


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ['user', 'word_ru', 'word_en']
    list_display_links = ['word_ru']


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username']


