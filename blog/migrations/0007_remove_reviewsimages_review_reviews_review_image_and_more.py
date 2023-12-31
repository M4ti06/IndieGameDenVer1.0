# Generated by Django 4.2.4 on 2023-11-11 20:50

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_reviewsminiaturesimages_miniature_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviewsimages",
            name="review",
        ),
        migrations.AddField(
            model_name="reviews",
            name="review_image",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.reviewsimages",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="reviewsimages",
            name="image",
            field=models.ImageField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="blog/media/reviews_images"
                ),
                upload_to="",
            ),
        ),
    ]
