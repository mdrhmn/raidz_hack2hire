# Generated by Django 3.1.6 on 2021-02-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210203_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventproposal',
            name='virtual',
            field=models.BooleanField(default=False),
        ),
    ]
