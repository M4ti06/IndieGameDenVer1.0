from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import PendingPremieres, Reviews, Rankings

# Create your models here.


class UserReviewsToRead(models.Model):
    Reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)


class UserFavouriteRankings(models.Model):
    Rankings = models.ForeignKey(Rankings, on_delete=models.CASCADE)


class UserPendingPremieres(models.Model):
    Premieres = models.ForeignKey(PendingPremieres, on_delete=models.CASCADE)


class UserProfile(models.Model):
    reviews_to_read = models.ForeignKey(UserReviewsToRead,on_delete=models.CASCADE, null=True)
    favourite_rankings = models.ForeignKey(UserFavouriteRankings,on_delete=models.CASCADE, null=True)
    pending_premieres = models.ForeignKey(UserPendingPremieres,on_delete=models.CASCADE, null=True)
    number_of_comments = models.IntegerField(default=0)
    rank = models.IntegerField(default=1)
    avatar = models.ImageField(upload_to="avatars/", height_field=50, width_field=50)

class CustomUser(AbstractUser):

    username = models.CharField(
        "username",
        max_length=150,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=False
    )



