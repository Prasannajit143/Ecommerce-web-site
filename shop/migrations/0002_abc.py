# Generated by Django 4.0.3 on 2022-12-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(default='', max_length=4000)),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=80)),
                ('address', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=80)),
            ],
        ),
    ]
