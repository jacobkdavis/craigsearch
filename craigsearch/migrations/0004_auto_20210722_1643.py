# Generated by Django 3.2.5 on 2021-07-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigsearch', '0003_auto_20210722_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searcharea',
            name='description',
        ),
        migrations.AddField(
            model_name='searcharea',
            name='areas',
            field=models.CharField(default='', max_length=1200),
        ),
    ]