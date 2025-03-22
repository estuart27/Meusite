# Generated by Django 5.1 on 2025-03-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnePage', '0006_portfolioitem_link_alter_portfolioitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
