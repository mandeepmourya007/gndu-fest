# Generated by Django 2.1.4 on 2019-04-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20190404_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_registered_events',
            name='event_name',
        ),
        migrations.AddField(
            model_name='student_registered_events',
            name='event_name',
            field=models.ManyToManyField(to='events.event'),
        ),
    ]
