# Generated by Django 3.1.1 on 2020-09-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20200919_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
