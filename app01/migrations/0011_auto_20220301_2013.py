# Generated by Django 3.2.10 on 2022-03-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20220223_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navs',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='navs',
            name='nav_category',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar_url',
            field=models.URLField(blank=True, help_text='可能是其他平台的头像', null=True, verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sign_status',
            field=models.IntegerField(choices=[(0, '用户名注册'), (1, 'QQ注册'), (2, 'gitee注册'), (3, '手机号注册'), (4, '邮箱注册')], default=0, verbose_name='注册方式'),
        ),
        migrations.DeleteModel(
            name='NavCategory',
        ),
    ]
