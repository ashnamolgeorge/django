# Generated by Django 4.1.4 on 2024-02-14 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaltrust', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='contact',
            field=models.IntegerField(default=0),
        ),
    ]
