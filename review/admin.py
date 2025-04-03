from django.contrib import admin
from django.forms import SlugField
from .models import Review

'''Fazendo a tabela 'review' conseguir ser alterada '''
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title","status", "rating", "published_ad","author", "slugfied_title"]
    list_filter = ["title", "status", "author"]   
    search_fields = ["title", "body", "author__username"]
    prepopulated_fields = {"slugfied_title": ["title"]}