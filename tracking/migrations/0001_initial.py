# Generated by Django 3.0.7 on 2020-06-20 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('_id', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=50)),
                ('tracking', models.CharField(blank=True, max_length=20)),
                ('ship_date', models.DateField(blank=True)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.Award')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.Member')),
            ],
        ),
    ]
