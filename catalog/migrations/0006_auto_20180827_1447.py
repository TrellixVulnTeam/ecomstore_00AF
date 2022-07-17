# Generated by Django 2.0.4 on 2018-08-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180827_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_caption',
            field=models.CharField(default='DEFAULT VALUE', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='images/products/thumbnails'),
        ),
    ]
