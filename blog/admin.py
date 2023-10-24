from django.contrib import admin
from blog import models
# Register your models here.

admin.site.register(models.Reviews)
admin.site.register(models.ReviewsComments)
admin.site.register(models.ReviewsVideo)
admin.site.register(models.ReviewsImages)
admin.site.register(models.ReviewsMiniaturesImages)
admin.site.register(models.Rankings)
admin.site.register(models.RankingsVideo)
admin.site.register(models.RankingsImages)
admin.site.register(models.RankingsComments)
admin.site.register(models.RankingsMiniaturesImages)
admin.site.register(models.QuestionnaireItems)
admin.site.register(models.Questionnaire)
admin.site.register(models.QuestionnaireItemsSummary)
admin.site.register(models.PendingPremieres)
admin.site.register(models.PremieresVideo)
admin.site.register(models.PremieresImages)
admin.site.register(models.PremieresComments)
admin.site.register(models.PremieresMiniaturesImages)
admin.site.register(models.Newsroom)
admin.site.register(models.NewsroomComments)
admin.site.register(models.NewsroomImages)
admin.site.register(models.NewsroomVideo)
admin.site.register(models.NewsroomMiniaturesImages)
admin.site.register(models.UserGameRatings)