# Generated by Django 4.2.7 on 2023-11-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftlist', '0008_alter_gift_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]