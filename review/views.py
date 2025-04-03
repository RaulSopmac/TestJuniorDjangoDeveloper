from django.shortcuts import render, get_object_or_404
from .models import Review

def review_list(request): 
    reviews = Review.published.all()
    return render(request, "review/list.html", {"reviews": reviews})    

def review_detail(request, year, month, day, slugfied_title):
    '''basicamento isso faz retornar um erro 404 e não um error 500 de servidor igual antes'''
    review: Review = get_object_or_404(
        Review.published, 
        published_ad__year=year,
        published_ad__month=month, 
        published_ad__day=day, 
        slugfied_title = slugfied_title
        )   
        
    return render(request, "review/detail.html", {"review": review})