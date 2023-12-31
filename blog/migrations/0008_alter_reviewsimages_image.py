# Generated by Django 4.2.4 on 2023-11-13 17:57

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_remove_reviewsimages_review_reviews_review_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewsimages",
            name="image",
            field=models.ImageField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="blog/media/reviews_images"
                ),
                upload_to="reviews_images",
            ),
        ),
    ]
