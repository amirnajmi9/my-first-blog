# Generated by Django 3.1.2 on 2020-10-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201017_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vrf',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
