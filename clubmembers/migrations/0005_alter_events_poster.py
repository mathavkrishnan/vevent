# Generated by Django 4.0 on 2022-02-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubmembers', '0004_events_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='poster',
            field=models.ImageField(default=False, upload_to='veventz/images/'),
        ),
    ]
