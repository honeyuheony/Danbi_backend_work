# Generated by Django 4.1.2 on 2022-10-10 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0002_alter_routine_account_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Routine_day',
            new_name='Day',
        ),
        migrations.RenameModel(
            old_name='Routine_result',
            new_name='Result',
        ),
    ]
