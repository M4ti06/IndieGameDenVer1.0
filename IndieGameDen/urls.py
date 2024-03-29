"""
URL configuration for IndieGameDen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("reviews", views.ReviewsListView.as_view(), name="reviews"),
    path("reviews/article/<pk>", views.ReviewsDetailView.as_view(), name="reviews-detail"),
    path("premieres", views.PremieresListView.as_view(), name="premieres"),
    path("premieres/article/<pk>", views.PremieresDetailView.as_view(), name="premieres-detail"),
    path("newsroom", views.NewsroomListView.as_view(), name="newsroom"),
    path("newsroom/article/<pk>", views.NewsroomDetailView.as_view(), name="newsroom-detail"),
    path("rankings", views.RankingListView.as_view(), name="rankings"),
    path("rankings/article/<pk>", views.RankingDetailView.as_view(), name="rankings-detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
