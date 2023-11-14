# Generated by Django 4.2.4 on 2023-11-14 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_alter_newsroomimages_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reviews",
            name="review_image",
        ),
        migrations.AddField(
            model_name="reviewsimages",
            name="review",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.reviews",
            ),
            preserve_default=False,
        ),
    ]
