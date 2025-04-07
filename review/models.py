from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone


class PublishedManage(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status='10')
     
class Review(models.Model):
    '''Usando 5 e 10 pois caso tenha alguma implementação posterior no codigo como 
    um delete ou review de published temos espaço para colocar outros dados '''
    class status(models.IntegerChoices):
        DRAFT = (5,"Draft")
        PUBLISHED = (10,"Published")

    class RatingChoices(models.IntegerChoices):
        BAD = (0,"0 - BAD")
        POOR = (1,"1 - POOR")
        FAIR = (2,"2 - FAIR")
        GOOD = (3,"3 - GOOD")
        EXCELLENT = (4,"4 - EXCELLENT")
        EXCEPTIONAL = (5,"5 - EXCEPTIONAL")

    title = models.CharField(max_length=200)
    slugfied_title = models.SlugField(max_length=200, unique_for_date="published_ad")
    status = models.IntegerField(choices=status.choices, default=status.DRAFT)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.GOOD)
    id = int 
    
    published_ad = models.DateTimeField(default=timezone.now)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManage()
    comments: models.Manager["Comment"]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("reviews:review_detail", 
                       args=[self.published_ad.year, self.published_ad.month,
                                   self.published_ad.day,self.slugfied_title]) 

    def __str__(self) -> str:
        return f"{self.title} - Status: {self.status} - Rating: {self.rating}"
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    message = models.TextField(max_length=400)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

