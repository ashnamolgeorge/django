# Generated by Django 4.1.4 on 2024-02-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaltrust', '0007_remove_myac_status_myac_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myac',
            name='message',
        ),
        migrations.AddField(
            model_name='myac',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]