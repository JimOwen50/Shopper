# Generated by Django 4.2.7 on 2023-11-16 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftlist', '0006_rename_gift_for_gift_purchased_by_member_gifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='gifts',
        ),
        migrations.AddField(
            model_name='gift',
            name='gift_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_gifts_for_member', to='giftlist.member'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='purchased_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_gift_purchaser', to='giftlist.member'),
        ),
    ]
