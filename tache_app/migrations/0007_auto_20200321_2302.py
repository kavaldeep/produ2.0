# Generated by Django 2.0 on 2020-03-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tache_app', '0006_auto_20200321_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='TempsAConsacrer',
            field=models.FloatField(null=True),
        ),
    ]