# Generated by Django 4.0.1 on 2022-02-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todo_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='difficulty',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='xp',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
