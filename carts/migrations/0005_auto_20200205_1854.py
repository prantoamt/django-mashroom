# Generated by Django 3.0.2 on 2020-02-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20200204_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(default='', max_length=120, unique=True)),
                ('charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(default='', max_length=120, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DeliveryCharge',
        ),
        migrations.AddField(
            model_name='area',
            name='district_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.District'),
        ),
    ]
