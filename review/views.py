from importlib.metadata import PackageNotFoundError
from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from .models import Review, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib import messages

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
    
    form = CommentForm()
    review: Review = get_object_or_404(
        Review.published, 
        published_ad__year=year,
        published_ad__month=month, 
        published_ad__day=day, 
        slugfied_title = slugfied_title
    )
    comments = review.comments.filter(active=True)
    
    return render(request, "review/detail.html", {"review": review, "form": form, "comments": comments})

@require_POST
def add_comment(request, review_id):
    
    review: Review = get_object_or_404(Review.published, id = review_id)
    form = CommentForm( data = request.POST )

    if form.is_valid():
        comment: Comment = form.save(commit=False)
        comment.review = review
        comment.save()
        messages.success(request, "Comment was added successfully!")
        return HttpResponseRedirect(review.get_absolute_url())
    else:
       return render(request, "review/detail.html", {"review": review, "form": form})

