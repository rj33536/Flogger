# Generated by Django 3.0.2 on 2020-03-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
