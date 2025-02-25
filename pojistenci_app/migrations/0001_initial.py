# Generated by Django 4.2.1 on 2025-02-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uzivatele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=40, verbose_name='Jméno')),
                ('prijmeni', models.CharField(max_length=40, verbose_name='Příjmení')),
                ('narozeni', models.DateField()),
                ('foto', models.CharField(max_length=60, verbose_name='Název souboru obrázku')),
                ('datum_registrace', models.DateField(auto_now=True)),
            ],
        ),
    ]
