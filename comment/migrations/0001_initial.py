# Generated by Django 3.0.4 on 2020-04-06 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('empresa', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('commentary', models.TextField()),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
