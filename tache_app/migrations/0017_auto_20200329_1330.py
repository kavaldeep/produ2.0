# Generated by Django 2.0 on 2020-03-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tache_app', '0016_auto_20200329_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='TempsCle',
            field=models.TextField(null=True),
        ),
    ]