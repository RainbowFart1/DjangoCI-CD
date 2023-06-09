# Generated by Django 3.2.10 on 2022-01-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_userinfo_collects'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='pwd',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='文章密码'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.IntegerField(blank=True, choices=[(0, '前端'), (1, '后端'), (2, '项目相关')], null=True, verbose_name='文章分类'),
        ),
    ]
