# Generated by Django 4.1.7 on 2023-02-23 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_coursefile_course_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursefile',
            name='course_file',
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Course-content')),
                ('course_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursefile')),
            ],
        ),
    ]
