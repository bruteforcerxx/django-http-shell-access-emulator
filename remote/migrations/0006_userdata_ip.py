# Generated by Django 3.0.6 on 2022-08-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0005_userdata_short_cuts'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='ip',
            field=models.CharField(default='', max_length=400),
        ),
    ]
