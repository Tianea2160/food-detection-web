# Generated by Django 3.2.6 on 2021-08-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210820_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionfacts',
            name='Foodname1',
            field=models.CharField(max_length=30),
        ),
    ]