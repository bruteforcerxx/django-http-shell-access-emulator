# Generated by Django 3.0.6 on 2022-08-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0003_alert_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='uid',
            field=models.CharField(default='0000000AAAAAAAAA', max_length=400),
        ),
    ]
