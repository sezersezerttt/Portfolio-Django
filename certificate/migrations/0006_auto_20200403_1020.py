# Generated by Django 3.0.4 on 2020-04-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0005_auto_20200403_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='certificate_image'),
        ),
    ]
