# Generated by Django 4.2.7 on 2023-11-18 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftlist', '0009_alter_gift_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite_gift_card',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_music_artist',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]