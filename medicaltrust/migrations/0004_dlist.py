# Generated by Django 4.1.4 on 2024-02-15 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaltrust', '0003_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=60)),
                ('qualification', models.CharField(max_length=50)),
            ],
        ),
    ]
