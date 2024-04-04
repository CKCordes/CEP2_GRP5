# Generated by Django 5.0.3 on 2024-04-04 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KitchenGuardServer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='patient',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='KitchenGuardServer.patient'),
            preserve_default=False,
        ),
    ]
