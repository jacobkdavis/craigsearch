# Generated by Django 3.2.5 on 2021-07-22 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('craigsearch', '0008_auto_20210722_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquery',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='craigsearch.searcharea'),
        ),
    ]
