# Generated by Django 5.1.4 on 2025-01-25 13:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_seller_phone_no'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='Email',
        ),
        migrations.AddField(
            model_name='seller',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='seller',
            name='bank_account_details',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='business_category',
            field=models.CharField(choices=[('WHOLE_SELLER', 'Whole Seller'), ('SUPPLIER', 'Supplier'), ('RETAILER', 'Retailer'), ('FARMER', 'Farmer')], default='FARMER', max_length=20),
        ),
        migrations.AddField(
            model_name='seller',
            name='business_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='county',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='seller',
            name='image',
            field=models.ImageField(blank=True, upload_to='seller_images'),
        ),
        migrations.AddField(
            model_name='seller',
            name='preferred_payment_methods',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='premium_subscription_expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='social_media_links',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='total_earnings',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='seller',
            name='total_products_sold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seller',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seller',
            name='town',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='seller',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seller',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='General_Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
