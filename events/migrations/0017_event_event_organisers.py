# Generated by Django 2.1.7 on 2019-04-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('events', '0016_remove_event_event_organisers'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_organisers',
            field=models.ManyToManyField(to='accounts.studentsignup'),
        ),
    ]