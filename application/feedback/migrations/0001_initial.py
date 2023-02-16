# Generated by Django 4.1.6 on 2023-02-16 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('☆☆☆☆☆', '☆☆☆☆☆'), ('☆☆☆☆', '☆☆☆☆'), ('☆☆☆', '☆☆☆'), ('☆☆', '☆☆'), ('☆', '☆')], max_length=15)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('course_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_comment', to='feedback.comment')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment', to='course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
