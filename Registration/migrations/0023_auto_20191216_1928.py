# Generated by Django 2.2.7 on 2019-12-17 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0022_currenttimeslots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenttimeslots',
            name='last_update',
            field=models.DateField(default='1900-01-02'),
        ),
    ]