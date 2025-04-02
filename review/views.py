from django.shortcuts import render
from .models import Review 

def review_list(request):
    reviews = Review.objects.filter(status='10')
    return render(request, "review/list.html", {"reviews": reviews})    

def review_detail(request, id):
    review = Review.objects.get(id=id)
    return render(request, "review/detail.html", {"review": review})