# Generated by Django 4.2.14 on 2024-08-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="news_img",
            field=models.CharField(max_length=100),
        ),
    ]
