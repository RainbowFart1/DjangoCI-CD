# Generated by Django 3.2.10 on 2022-03-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20220301_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavTags',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=16, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '网站标签',
            },
        ),
        migrations.AddField(
            model_name='navs',
            name='collects_count',
            field=models.IntegerField(default=0, verbose_name='文章收藏数'),
        ),
        migrations.AddField(
            model_name='navs',
            name='digg_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AddField(
            model_name='navs',
            name='tag',
            field=models.ManyToManyField(to='app01.NavTags', verbose_name='网站标签'),
        ),
    ]
