# Generated by Django 5.0.6 on 2024-06-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.jpg', upload_to=''),
        ),
    ]