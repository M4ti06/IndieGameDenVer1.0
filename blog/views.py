from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from blog.models import Reviews


class HomeView(TemplateView):
    template_name = "home.html"


class ReviewsListView(ListView):
    model = Reviews
    queryset = Reviews.objects.order_by("date_of_publishing")
    context_object_name = "reviews"
    template_name = "reviews.html"


class ReviewsDetailView(DetailView):
    model = Reviews
    context_object_name = "review"
    template_name = "reviews-article.html"