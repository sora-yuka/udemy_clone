# Generated by Django 4.1.7 on 2023-02-16 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default='Education', on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='sub_title',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]