# Generated by Django 2.1.5 on 2019-03-10 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=64)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(default='all_covers/farm.jpg', upload_to='all_covers/')),
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
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='product_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='farmshop.Products'),
        ),
    ]