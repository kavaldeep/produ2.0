# Generated by Django 3.0.3 on 2020-09-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tache_app', '0026_auto_20200903_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='TempsAConsacrer',
            field=models.DurationField(null=True),
        ),
    ]