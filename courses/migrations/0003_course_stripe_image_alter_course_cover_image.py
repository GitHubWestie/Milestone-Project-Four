# Generated by Django 5.1.1 on 2024-10-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="stripe_image",
            field=models.URLField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name="course",
            name="cover_image",
            field=models.ImageField(upload_to="course-logo"),
        ),
    ]
