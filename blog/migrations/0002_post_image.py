# Generated by Django 3.1.2 on 2020-10-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1),
            preserve_default=False,
        ),
    ]
