from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from blog.models import Reviews, ReviewsImages, ReviewsVideo, ReviewsComments, PendingPremieres, PremieresVideo
from blog.models import PremieresComments, PremieresImages

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

    def get_context_data(self, **kwargs):
        context = super(ReviewsDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context["review_images"] = ReviewsImages.objects.filter(review=pk)
        context["review_videos"] = ReviewsVideo.objects.filter(review=pk)
        context["review_comments"] = ReviewsComments.objects.filter(game_review=pk)
        return context


class PremieresListView(ListView):
    model = PendingPremieres
    queryset = PendingPremieres.objects.order_by("date_of_publishing")
    context_object_name = "premieres"
    template_name = "premieres.html"


class PremieresDetailView(DetailView):
    model = PendingPremieres
    context_object_name = "premiere"
    template_name = "premieres-article.html"

    def get_context_data(self, **kwargs):
        context = super(PremieresDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context["premieres_images"] = PremieresImages.objects.filter(premiere=pk)
        context["premieres_videos"] = PremieresVideo.objects.filter(premiere=pk)
        context["premieres_comments"] = PremieresComments.objects.filter(premiere=pk)
        return context
