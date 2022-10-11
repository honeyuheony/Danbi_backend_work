# Generated by Django 4.1.2 on 2022-10-07 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('routine_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('account_id', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('MIRACLE', 'MIRACLE'), ('HOMEWORK', 'HOMEWORK')], max_length=10)),
                ('goal', models.CharField(max_length=200)),
                ('is_alarm', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routine_result',
            fields=[
                ('routine_result_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('result', models.CharField(choices=[('NOT', 'NOT'), ('TRY', 'TRY'), ('DONE', 'DONE')], default='NOT', max_length=10)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('routine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
        migrations.CreateModel(
            name='Routine_day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('routine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
    ]