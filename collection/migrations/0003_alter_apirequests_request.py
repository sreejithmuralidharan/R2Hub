# Generated by Django 3.2.5 on 2021-07-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20210730_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequests',
            name='request',
            field=models.JSONField(default=dict),
        ),
    ]
