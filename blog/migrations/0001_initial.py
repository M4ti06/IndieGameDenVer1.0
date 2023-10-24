# Generated by Django 4.2.4 on 2023-09-01 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Newsroom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=10000)),
                ("date_of_publishing", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="PendingPremieres",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=5000)),
                ("release_date", models.DateField()),
                ("will_play", models.IntegerField()),
                ("date_of_publishing", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Questionnaire",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("date_of_publishing", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="QuestionnaireItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title_of_item", models.CharField(max_length=100)),
                (
                    "questionnaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.questionnaire",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rankings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("date_of_publishing", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=10000)),
                ("game_rating", models.DecimalField(decimal_places=1, max_digits=2)),
                (
                    "game_user_rating",
                    models.DecimalField(decimal_places=1, max_digits=2),
                ),
                ("date_of_publishing", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="UserGameRatings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_game_rating",
                    models.DecimalField(decimal_places=1, max_digits=2),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewsVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to="reviews_videos/")),
                ("description", models.CharField(max_length=50)),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.reviews"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewsMiniaturesImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "miniature_image",
                    models.ImageField(upload_to="reviews_miniatures_images/"),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.reviews"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewsImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        height_field=200, upload_to="reviews_images/", width_field=200
                    ),
                ),
                ("description", models.CharField(max_length=50)),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.reviews"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewsComments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=400)),
                ("likes", models.IntegerField()),
                ("dislikes", models.IntegerField()),
                (
                    "game_review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.reviews"
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RankingsVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to="rankings_videos/")),
                ("description", models.CharField(max_length=50)),
                (
                    "ranking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.rankings"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RankingsMiniaturesImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "miniature_image",
                    models.ImageField(upload_to="rankings_miniatures_images/"),
                ),
                (
                    "ranking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.rankings"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RankingsImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        height_field=200, upload_to="rankings_images/", width_field=200
                    ),
                ),
                ("description", models.CharField(max_length=50)),
                (
                    "ranking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.rankings"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RankingsComments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=400)),
                ("likes", models.IntegerField()),
                ("dislikes", models.IntegerField()),
                (
                    "ranking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.rankings"
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionnaireItemsSummary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField()),
                (
                    "questionnaire_items",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.questionnaireitems",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PremieresVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to="premieres_videos/")),
                ("description", models.CharField(max_length=50)),
                (
                    "premiere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.pendingpremieres",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PremieresMiniaturesImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "miniature_image",
                    models.ImageField(upload_to="rankings_miniatures_images/"),
                ),
                (
                    "premiere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.pendingpremieres",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PremieresImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        height_field=200, upload_to="premieres_images/", width_field=200
                    ),
                ),
                ("description", models.CharField(max_length=50)),
                (
                    "premiere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.pendingpremieres",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PremieresComments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=400)),
                ("likes", models.IntegerField()),
                ("dislikes", models.IntegerField()),
                (
                    "premiere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.pendingpremieres",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsroomVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to="newsroom_videos/")),
                ("description", models.CharField(max_length=50)),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.newsroom"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsroomMiniaturesImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "miniature_image",
                    models.ImageField(upload_to="newsroom_miniatures_images/"),
                ),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.newsroom"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsroomImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        height_field=200, upload_to="newsroom_images/", width_field=200
                    ),
                ),
                ("description", models.CharField(max_length=50)),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.newsroom"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsroomComments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=400)),
                ("likes", models.IntegerField()),
                ("dislikes", models.IntegerField()),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.newsroom"
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
