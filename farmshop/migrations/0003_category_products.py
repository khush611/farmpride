# Generated by Django 2.1.5 on 2019-03-10 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmshop', '0002_auto_20190310_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('company_name', models.CharField(max_length=128)),
                ('product_price', models.IntegerField()),
                ('image', models.ImageField(upload_to='products')),
                ('product_desc', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('category_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='farmshop.Category')),
            ],
        ),
    ]