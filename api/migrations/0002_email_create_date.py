# Generated by Django 3.2.10 on 2022-03-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='发送时间'),
        ),
    ]
