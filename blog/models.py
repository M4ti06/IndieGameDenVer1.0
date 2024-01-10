from django.db import models
from IndieGameDen import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location="blog/media")


class Newsroom(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = models.CharField(max_length=10000)
    date_of_publishing = models.DateField()


class NewsroomImages(models.Model):
    image = models.ImageField(upload_to="newsroom_images", storage=fs)
    description = models.CharField(max_length=50)
    news = models.ForeignKey(Newsroom, on_delete=models.CASCADE)


class NewsroomVideo(models.Model):
    video = models.FileField(upload_to="newsroom_videos", storage=fs)
    description = models.CharField(max_length=50)
    news = models.ForeignKey(Newsroom, on_delete=models.CASCADE)


class NewsroomMiniaturesImages(models.Model):
    miniature_image = models.ImageField(upload_to="newsroom_miniatures_images", storage=fs)
    news = models.ForeignKey(Newsroom, on_delete=models.CASCADE)


class NewsroomComments(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    news = models.ForeignKey(Newsroom,on_delete=models.CASCADE)
    date_of_publishing = models.DateField()


class ReviewsMiniaturesImages(models.Model):
    miniature_image = models.ImageField(upload_to="reviews_miniatures_images", storage=fs)
    description = models.CharField(max_length=50)
    game_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.game_title} {self.description}"




class Reviews(models.Model):
    title = models.CharField(max_length=100)
    game_title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = models.CharField(max_length=10000)
    game_rating = models.DecimalField(max_digits=2, decimal_places=1)
    game_user_rating = models.DecimalField(max_digits=2, decimal_places=1)
    date_of_publishing = models.DateField()
    review_minature_image = models.ForeignKey(ReviewsMiniaturesImages, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.game_title}"


class ReviewsImages(models.Model):
    image = models.ImageField(upload_to="reviews_images", storage=fs)
    description = models.CharField(max_length=50)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)


class ReviewsVideo(models.Model):
    video = models.FileField(upload_to="reviews_videos", storage=fs)
    description = models.CharField(max_length=50)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}"



class ReviewsComments(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    game_review = models.ForeignKey(Reviews,on_delete=models.CASCADE)


class UserGameRatings(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_game_rating = models.DecimalField(max_digits=2, decimal_places=1)


class Rankings(models.Model):
    title = models.CharField(max_length=100)
    date_of_publishing = models.DateField()
    description = models.CharField(max_length=300)


class RankingsImages(models.Model):
    image = models.ImageField(upload_to="rankings_images", storage=fs)
    description = models.CharField(max_length=50)
    ranking = models.ForeignKey(Rankings, on_delete=models.CASCADE)


class RankingsVideo(models.Model):
    video = models.FileField(upload_to="rankings_videos", storage=fs)
    description = models.CharField(max_length=50)
    ranking = models.ForeignKey(Rankings, on_delete=models.CASCADE)


class RankingsMiniaturesImages(models.Model):
    miniature_image = models.ImageField(upload_to="rankings_miniatures_images", storage=fs)
    ranking = models.ForeignKey(Rankings, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)


class RankingsComments(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    ranking = models.ForeignKey(Rankings,on_delete=models.CASCADE)
    date_of_publishing = models.DateField()


class PremieresMiniaturesImages(models.Model):
    miniature_image = models.ImageField(upload_to="premieres_miniatures_images", storage=fs)
    description = models.CharField(max_length=50)
    game_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.game_title} {self.description}"

class PendingPremieres(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    content = models.CharField(max_length=10000)
    game_title = models.CharField(max_length=100)
    release_date = models.DateField()
    will_play = models.IntegerField()
    date_of_publishing = models.DateField()
    premiere = models.ForeignKey(PremieresMiniaturesImages, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.game_title}"


class PremieresImages(models.Model):
    image = models.ImageField(upload_to="premieres_images", storage=fs)
    description = models.CharField(max_length=50)
    premiere = models.ForeignKey(PendingPremieres, on_delete=models.CASCADE)


class PremieresVideo(models.Model):
    video = models.FileField(upload_to="premieres_videos", storage=fs)
    description = models.CharField(max_length=50)
    premiere = models.ForeignKey(PendingPremieres, on_delete=models.CASCADE)



class PremieresComments(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    premiere = models.ForeignKey(PendingPremieres,on_delete=models.CASCADE)
    date_of_publishing = models.DateField()


class Questionnaire(models.Model):
    title = models.CharField(max_length=100)
    date_of_publishing = models.DateField()


class QuestionnaireItems(models.Model):
    title_of_item = models.CharField(max_length=100)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)


class QuestionnaireItemsSummary(models.Model):
    score = models.IntegerField()
    questionnaire_items = models.ForeignKey(QuestionnaireItems,on_delete=models.CASCADE)