# Generated by Django 5.0.6 on 2024-06-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('ape', models.CharField(max_length=30)),
                ('idn', models.CharField(max_length=30)),
                ('sx', models.CharField(max_length=20)),
                ('fec', models.CharField(max_length=20)),
                ('dirc', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('cor', models.CharField(max_length=30)),
            ],
        ),
    ]