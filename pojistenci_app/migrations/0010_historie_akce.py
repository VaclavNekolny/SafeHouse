# Generated by Django 4.2.1 on 2025-02-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojistenci_app', '0009_alter_historie_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historie',
            name='akce',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
