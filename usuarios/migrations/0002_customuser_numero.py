# Generated by Django 4.2 on 2023-04-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='numero',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Numero para votacao'),
        ),
    ]