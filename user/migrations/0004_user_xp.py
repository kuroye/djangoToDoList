# Generated by Django 4.0.1 on 2022-02-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_level_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]