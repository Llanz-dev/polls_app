# Generated by Django 4.1 on 2022-08-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_poll_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='vote_img'),
        ),
    ]
