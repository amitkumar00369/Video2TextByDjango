# Generated by Django 5.1.1 on 2024-09-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("converter", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videofile",
            name="video",
            field=models.FileField(upload_to="download/"),
        ),
    ]
