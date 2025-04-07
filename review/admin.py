from django.contrib import admin
from django.forms import SlugField
from .models import Review, Comment

'''Fazendo a tabela 'review' conseguir ser alterada '''
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title","status", "rating", "published_ad","author", "slugfied_title"]
    list_filter = ["title", "status", "author"]   
    search_fields = ["title", "body", "author__username"]
    prepopulated_fields = {"slugfied_title": ["title"]}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["review","user_name", "user_email", "message","active"]
    list_filter = ["user_name", "active", "created_at"]   
    search_fields = ["user_name", "active", "created_at"]
    '''prepopulated_fields = {"slugfied_title": ["title"]}'''