# Generated by Django 4.1.7 on 2023-03-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_userprofile_followers_userprofile_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
