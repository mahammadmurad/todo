# Generated by Django 4.2.6 on 2023-10-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_todo_dead_time_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
