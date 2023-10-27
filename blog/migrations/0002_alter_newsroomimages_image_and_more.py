# Generated by Django 4.2.4 on 2023-10-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsroomimages",
            name="image",
            field=models.ImageField(
                height_field=200,
                upload_to="blog/static/newsroom_images/",
                width_field=200,
            ),
        ),
        migrations.AlterField(
            model_name="newsroomminiaturesimages",
            name="miniature_image",
            field=models.ImageField(
                upload_to="blog/static/newsroom_miniatures_images/"
            ),
        ),
        migrations.AlterField(
            model_name="newsroomvideo",
            name="video",
            field=models.FileField(upload_to="blog/static/newsroom_videos/"),
        ),
        migrations.AlterField(
            model_name="premieresimages",
            name="image",
            field=models.ImageField(
                height_field=200,
                upload_to="blog/static/premieres_images/",
                width_field=200,
            ),
        ),
        migrations.AlterField(
            model_name="premieresminiaturesimages",
            name="miniature_image",
            field=models.ImageField(
                upload_to="blog/static/rankings_miniatures_images/"
            ),
        ),
        migrations.AlterField(
            model_name="premieresvideo",
            name="video",
            field=models.FileField(upload_to="blog/static/premieres_videos/"),
        ),
        migrations.AlterField(
            model_name="rankingsimages",
            name="image",
            field=models.ImageField(
                height_field=200,
                upload_to="blog/static/rankings_images/",
                width_field=200,
            ),
        ),
        migrations.AlterField(
            model_name="rankingsminiaturesimages",
            name="miniature_image",
            field=models.ImageField(
                upload_to="blog/static/rankings_miniatures_images/"
            ),
        ),
        migrations.AlterField(
            model_name="rankingsvideo",
            name="video",
            field=models.FileField(upload_to="blog/static/rankings_videos/"),
        ),
        migrations.AlterField(
            model_name="reviewscomments",
            name="dislikes",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="reviewscomments",
            name="likes",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="reviewsimages",
            name="image",
            field=models.ImageField(upload_to="blog/static/reviews_images/"),
        ),
        migrations.AlterField(
            model_name="reviewsminiaturesimages",
            name="miniature_image",
            field=models.ImageField(upload_to="blog/static/reviews_miniatures_images/"),
        ),
        migrations.AlterField(
            model_name="reviewsvideo",
            name="video",
            field=models.FileField(upload_to="blog/static/reviews_videos/"),
        ),
    ]