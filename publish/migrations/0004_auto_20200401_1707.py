# Generated by Django 3.0.4 on 2020-04-01 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0003_auto_20200401_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publish',
            old_name='publish_name',
            new_name='name',
        ),
    ]
