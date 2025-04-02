from django.contrib import admin
from .models import Review

'''Fazendo a tabela 'review' conseguir ser alterada '''
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title","status", "rating", "published_ad","author"]
    list_filter = ["title", "status", "author"]   
    search_fields = ["title", "body", "author__username"]