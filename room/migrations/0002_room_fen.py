# Generated by Django 3.1.5 on 2021-01-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='fen',
            field=models.TextField(null=True),
        ),
    ]
