# Generated by Django 3.0.1 on 2019-12-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0002_auto_20191227_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_place',
            name='bus_duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add_place',
            name='flight_duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add_place',
            name='train_duration',
            field=models.IntegerField(),
        ),
    ]