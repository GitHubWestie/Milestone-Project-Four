# Generated by Django 5.1.1 on 2024-10-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_course_stripe_image_alter_course_cover_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="stripe_image",
            field=models.URLField(blank=True, max_length=512),
        ),
    ]
