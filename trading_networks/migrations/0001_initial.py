# Generated by Django 5.0.2 on 2024-03-03 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_type', models.CharField(choices=[('Factory', 'Factory'), ('RetailNetwork', 'RetailNetwork'), ('IndividualBusinessman', 'IndividualBusinessman')], max_length=35, verbose_name='network type')),
                ('network_level', models.IntegerField(default=0, verbose_name='level in the hierarchy')),
                ('name', models.CharField(max_length=150, verbose_name='network name')),
                ('email', models.EmailField(max_length=254, verbose_name='email of the network')),
                ('country', models.CharField(max_length=80, verbose_name='country')),
                ('city', models.CharField(max_length=80, verbose_name='city')),
                ('street', models.CharField(max_length=80, verbose_name='street')),
                ('house_number', models.CharField(max_length=30, verbose_name='house number')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='debt')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date of creation')),
                ('products', models.ManyToManyField(to='products.product', verbose_name='product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trading_networks.network', verbose_name='supplier')),
            ],
            options={
                'verbose_name': 'network',
                'verbose_name_plural': 'networks',
            },
        ),
    ]
