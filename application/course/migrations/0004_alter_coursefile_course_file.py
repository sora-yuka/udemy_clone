# Generated by Django 4.1.7 on 2023-02-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefile',
            name='course_file',
            field=models.FileField(upload_to='course-content/'),
        ),
    ]