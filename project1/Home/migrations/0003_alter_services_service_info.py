# Generated by Django 4.2.14 on 2024-08-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Home", "0002_services"),
    ]

    operations = [
        migrations.AlterField(
            model_name="services",
            name="service_info",
            field=models.CharField(max_length=400),
        ),
    ]