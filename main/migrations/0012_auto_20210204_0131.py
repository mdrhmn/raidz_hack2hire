# Generated by Django 3.1.6 on 2021-02-03 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_eventproposal_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventproposal',
            old_name='date',
            new_name='month',
        ),
    ]
