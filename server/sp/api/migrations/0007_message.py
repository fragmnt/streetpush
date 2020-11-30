# Generated by Django 3.1.3 on 2020-11-26 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201123_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now=True)),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.citizen')),
            ],
        ),
    ]
