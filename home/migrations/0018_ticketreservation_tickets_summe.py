# Generated by Django 2.0.2 on 2018-04-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20180406_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketreservation',
            name='tickets_summe',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
