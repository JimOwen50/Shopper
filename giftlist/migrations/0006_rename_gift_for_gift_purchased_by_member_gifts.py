# Generated by Django 4.2.7 on 2023-11-16 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftlist', '0005_remove_gift_is_shopper_member_is_shopper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='gift_for',
            new_name='purchased_by',
        ),
        migrations.AddField(
            model_name='member',
            name='gifts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='giftlist.gift'),
        ),
    ]
