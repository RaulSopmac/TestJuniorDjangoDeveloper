from importlib.metadata import PackageNotFoundError
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from .models import Review

def review_list(request): 
    reviews = Review.published.all()
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get("page", 1)
    try:
        review_page = paginator.page(page_number)
    except (PageNotAnInteger,EmptyPage):
        review_page = paginator.page(1)
    return render(request, "review/list.html", {"review_page": review_page})    

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