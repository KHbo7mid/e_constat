# Generated by Django 5.0.3 on 2024-03-28 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assure',
            fields=[
                ('numr_tlfn', models.IntegerField(primary_key=True, serialize=False)),
                ('email_user', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('num_permis', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Constat',
            fields=[
                ('id_constat', models.AutoField(primary_key=True, serialize=False)),
                ('assure', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Conducteur',
            fields=[
                ('numr_tlfn', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('num_permis', models.IntegerField()),
                ('assure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conductor', to='api.assure')),
            ],
        ),
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu_accident', models.CharField(max_length=255)),
                ('date_accident', models.DateField()),
                ('constat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accident', to='api.constat')),
            ],
        ),
        migrations.CreateModel(
            name='Degat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='degat_photos/')),
                ('description', models.TextField(blank=True, null=True)),
                ('peinture', models.ImageField(blank=True, null=True, upload_to='peinture_photos/')),
                ('accident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='degat', to='api.accident')),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('carte_grise', models.IntegerField(primary_key=True, serialize=False)),
                ('immatriculation', models.IntegerField()),
                ('marque', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('constat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voiture', to='api.constat')),
            ],
        ),
    ]
