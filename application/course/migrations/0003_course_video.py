# Generated by Django 4.1.7 on 2023-02-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(default=1, upload_to='Video-content/'),
            preserve_default=False,
        ),
    ]
