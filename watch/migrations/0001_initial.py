# Generated by Django 3.2.9 on 2022-01-03 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_type', models.CharField(max_length=30)),
                ('special', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='watches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='photo')),
                ('des', models.CharField(max_length=50)),
                ('watch_type', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='watch.category')),
            ],
        ),
    ]
