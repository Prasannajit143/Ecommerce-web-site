# Generated by Django 4.0.3 on 2023-01-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
