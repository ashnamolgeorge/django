# Generated by Django 4.1.4 on 2024-02-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaltrust', '0005_alter_contacts_phone_myac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myac',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
