# Generated by Django 4.1.7 on 2023-04-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]
