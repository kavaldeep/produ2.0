# Generated by Django 2.0 on 2020-03-21 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Etat', models.CharField(max_length=100)),
                ('Deadline', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
