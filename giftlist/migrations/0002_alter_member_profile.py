# Generated by Django 4.2.7 on 2023-11-16 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='giftlist.profile'),
        ),
    ]
