# Generated by Django 2.0 on 2020-03-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tache_app', '0007_auto_20200321_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='Etat',
            field=models.CharField(choices=[('A faire', 'A faire'), ('En Cours', 'En Cours'), ('Finis', 'Finis')], max_length=100),
        ),
    ]
