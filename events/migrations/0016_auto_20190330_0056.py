# Generated by Django 2.1.4 on 2019-03-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190330_0056'),
        ('events', '0015_auto_20190315_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_organisers',
        ),
        migrations.AddField(
            model_name='event',
            name='event_organisers',
            field=models.ManyToManyField(to='accounts.studentsignup'),
        ),
    ]
