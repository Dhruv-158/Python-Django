# Generated by Django 4.2.16 on 2024-09-16 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Home", "0003_alter_services_service_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cone",
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
                ("Cone_img", models.CharField(max_length=60)),
                ("Cone_Title", models.CharField(max_length=300)),
                ("Cone_Des", models.CharField(max_length=1000)),
            ],
        ),
    ]
