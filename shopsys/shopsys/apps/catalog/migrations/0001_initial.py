# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='名称', max_length=50)),
                ('slug', models.SlugField(help_text='根据name生成的，用于生成页面URL，必须唯一', unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('meta_keywords', models.CharField(help_text='meta关键词，有利于SEO， 用逗号分隔', verbose_name='Meta 关键词', max_length=255)),
                ('meta_description', models.CharField(help_text='meta描述', verbose_name='Meta 描述', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'categories',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, verbose_name='名称', max_length=255)),
                ('slug', models.SlugField(help_text='根据name生成的，用于生成页面URL，必须唯一', unique=True, verbose_name='Slug', max_length=255)),
                ('brand', models.CharField(verbose_name='品牌', max_length=50)),
                ('sku', models.CharField(verbose_name='计量单位', max_length=50)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2, verbose_name='价格')),
                ('old_price', models.DecimalField(max_digits=9, decimal_places=2, default=0.0, verbose_name='旧价格', blank=True)),
                ('image', models.ImageField(upload_to='products', verbose_name='图片', max_length=50)),
                ('is_active', models.BooleanField(default=True, verbose_name='设为激活')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name='标为畅销')),
                ('is_featured', models.BooleanField(default=False, verbose_name='标为推荐')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述')),
                ('meta_keywords', models.CharField(help_text='meta 关键词标签, 逗号分隔', verbose_name='Meta关键词', max_length=255)),
                ('meta_description', models.CharField(help_text='meta 描述标签', verbose_name='Meta描述', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]
