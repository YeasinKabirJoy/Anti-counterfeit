# Generated by Django 4.0 on 2022-01-20 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carton',
            fields=[
                ('carton_id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('product_quantity', models.IntegerField()),
                ('production_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('distributor_scan_date', models.DateField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('pharmacist_details', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_scan', models.IntegerField(blank=True, default=0, null=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('delivery_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delivery', to='userManagement.deliveryperson')),
                ('distributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='distributor', to='userManagement.distributor')),
                ('manufacturer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userManagement.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('number_of_scan', models.IntegerField(blank=True, default=0, null=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('carton_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.carton')),
            ],
        ),
    ]