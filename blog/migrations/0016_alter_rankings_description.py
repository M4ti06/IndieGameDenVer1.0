# Generated by Django 4.2.4 on 2024-01-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0015_remove_rankingsminiaturesimages_ranking_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rankings",
            name="description",
            field=models.CharField(max_length=10000),
        ),
    ]
