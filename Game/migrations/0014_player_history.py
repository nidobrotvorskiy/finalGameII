# Generated by Django 3.1 on 2021-05-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0013_auto_20210513_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='History',
            field=models.CharField(default='[200]', max_length=400, verbose_name='history'),
        ),
    ]
