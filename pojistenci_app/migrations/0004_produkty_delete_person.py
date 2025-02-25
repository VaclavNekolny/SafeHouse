# Generated by Django 4.2.1 on 2025-02-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojistenci_app', '0003_person_alter_pojistenci_foto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produkty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=80, verbose_name='Název pojištění')),
                ('predmet_kryti', models.CharField(max_length=200, verbose_name='Předmět krytí')),
                ('zakladni_castka', models.IntegerField(verbose_name='Základní částka krytí')),
                ('zakladni_cena', models.IntegerField(verbose_name='Základní cena')),
                ('pomer', models.FloatField(verbose_name='Poměr mezi částkou krytí a cenou pojištění')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
