# Generated by Django 3.1.3 on 2020-11-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='citizen_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notif_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
