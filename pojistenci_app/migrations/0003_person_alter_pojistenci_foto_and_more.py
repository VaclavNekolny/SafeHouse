# Generated by Django 4.2.1 on 2025-02-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojistenci_app', '0002_rename_uzivatele_pojistenci'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='pojistenci',
            name='foto',
            field=models.CharField(max_length=60, verbose_name='Název obrázku'),
        ),
        migrations.AlterField(
            model_name='pojistenci',
            name='narozeni',
            field=models.DateField(verbose_name='Datum narození'),
        ),
    ]
