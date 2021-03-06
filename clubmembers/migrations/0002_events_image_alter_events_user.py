# Generated by Django 4.0 on 2022-02-04 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubmembers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(default=True, upload_to='veventz/images/'),
        ),
        migrations.AlterField(
            model_name='events',
            name='user',
            field=models.ForeignKey(db_constraint=False, default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
