# Generated by Django 2.0.4 on 2018-08-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchterm',
            name='tracking_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
