# Generated by Django 4.2.7 on 2023-11-16 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_size', models.CharField(blank=True, max_length=50, null=True)),
                ('pants_size', models.CharField(blank=True, max_length=50, null=True)),
                ('shoe_size', models.CharField(blank=True, max_length=50, null=True)),
                ('favorite_color', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftlist.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('retailer', models.CharField(blank=True, max_length=200, null=True)),
                ('retailer_link', models.URLField(blank=True, help_text='For example: the link to an item on Amazon.', null=True)),
                ('qty_asked_for', models.IntegerField(default=1, null=True)),
                ('qty_purchased', models.IntegerField(blank=True, default=0, null=True)),
                ('purchased', models.IntegerField(blank=True, default=0, null=True)),
                ('estimated_price', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Purchased', 'Purchased')], default='Available', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='giftlist.category')),
                ('gift_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('purchased_by', models.ForeignKey(blank=True, db_column='first_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='giftlist.member')),
            ],
        ),
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('member_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='giftlist.member')),
                ('favorite_coffee', models.CharField(blank=True, max_length=200, null=True)),
                ('purchased_gifts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='giftlist.gift')),
            ],
            bases=('giftlist.member',),
        ),
    ]
