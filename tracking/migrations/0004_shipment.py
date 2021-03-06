# Generated by Django 3.0.7 on 2020-07-15 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_delete_shipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking', models.CharField(blank=True, max_length=20)),
                ('ship_date', models.DateField(blank=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.Address')),
                ('award', models.ManyToManyField(to='tracking.Award')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.Member')),
            ],
        ),
    ]
