# Generated by Django 2.1.4 on 2019-03-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_event_organisers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
