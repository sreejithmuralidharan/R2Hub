# Generated by Django 3.2.5 on 2021-07-30 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_rename_request_apirequests_request_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequests',
            name='request_data',
            field=models.JSONField(default=list),
        ),
    ]