# Generated by Django 4.2.1 on 2023-05-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.EmailField(max_length=50)),
                ("select_service", models.CharField(max_length=50)),
                ("select_price", models.CharField(max_length=50)),
                ("comments", models.CharField(max_length=200)),
            ],
        ),
    ]
