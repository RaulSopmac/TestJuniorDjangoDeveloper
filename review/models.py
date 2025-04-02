from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Review(models.Model):
    '''Usando 5 e 10 pois caso tenha alguma implementação posterior no codigo como 
    um delete ou review de published temos espaço para colocar outros dados '''
    class status(models.IntegerChoices):
        DRAFT = (5,"Draft")
        PUBLISHED = (10,"Published")

    class RatingChoices(models.IntegerChoices):
        BAD = (0,"0 - BAD")
        POOR = (1,"1 = POOR")
        FAIR = (2,"2 - FAIR")
        GOOD = (3,"3 - GOOD")
        EXCELLENT = (4,"4 - EXCELLENT")
        EXCEPTIONAL = (5,"5 - EXCEPTIONAL")

    title = models.CharField(max_length=200)
    status = models.IntegerField(choices=status.choices, default=status.DRAFT)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.GOOD)
    
    published_ad = models.DateTimeField(default=timezone.now)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} - Status: {self.status} - Rating: {self.rating}"
