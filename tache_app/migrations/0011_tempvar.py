# Generated by Django 2.0 on 2020-03-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tache_app', '0010_auto_20200327_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempvar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Etat', models.TextField()),
            ],
        ),
    ]