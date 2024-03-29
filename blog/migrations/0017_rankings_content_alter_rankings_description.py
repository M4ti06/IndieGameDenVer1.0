# Generated by Django 4.2.4 on 2024-01-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_alter_rankings_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="rankings",
            name="content",
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="rankings",
            name="description",
            field=models.CharField(max_length=300),
        ),
    ]
