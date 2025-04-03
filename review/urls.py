from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.review_list, name="review_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slugfied_title>", views.review_detail, name="review_detail")
]