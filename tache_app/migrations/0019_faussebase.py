# Generated by Django 2.0 on 2020-03-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tache_app', '0018_auto_20200329_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='FausseBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TempsList', models.CharField(max_length=100)),
            ],
        ),
    ]
