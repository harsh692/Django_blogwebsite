# Generated by Django 4.2.4 on 2023-08-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read the blogpost.', max_length=255),
        ),
    ]
