# Generated by Django 2.2.4 on 2019-09-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callhubapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_result',
            name='Fibonacci_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_result',
            name='TimeTaken_exe',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]