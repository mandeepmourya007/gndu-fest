# Generated by Django 2.1.4 on 2019-04-03 16:11
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190315_1512'),
    ]
def gen_uuid(apps, schema_editor):
    for row in studentsignup.objects.all():
        row.email_id = uuid.uuid4()
        row.save()
        
    operations = [
        migrations.AlterField(
            model_name='studentsignup',
            name='email_id',
            field=models.EmailField(max_length=40, unique=True,default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='last_name',
            field=models.CharField(default=' ', max_length=60),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
