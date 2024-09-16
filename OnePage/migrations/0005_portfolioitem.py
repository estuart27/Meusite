# Generated by Django 5.1 on 2024-09-05 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnePage', '0004_rename_mensagem_mensagem_mensagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='portfolio/thumbnails/')),
            ],
        ),
    ]