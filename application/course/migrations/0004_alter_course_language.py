# Generated by Django 4.1.7 on 2023-02-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_category_category_alter_course_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.CharField(choices=[('Русский', 'Русский'), ('English', 'English'), ('Hindi', 'Hindi')], max_length=25),
        ),
    ]
