# Generated by Django 3.0.4 on 2020-04-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0006_auto_20200403_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=500)),
                ('contact_email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
    ]
