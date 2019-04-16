# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-19 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='商品数量')),
                ('status', models.IntegerField(choices=[(0, '禁用'), (-1, '删除'), (1, '正常')], default=1)),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=32, verbose_name='订单号')),
                ('order_time', models.DateTimeField()),
                ('order_status', models.IntegerField(choices=[(0, '禁用'), (-1, '删除'), (1, '正常')], default=1)),
                ('total_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30, verbose_name='商品名称')),
                ('product_price', models.FloatField(null=True, verbose_name='商品价格')),
                ('product_num', models.IntegerField(null=True, verbose_name='商品数量')),
                ('product_img', models.ImageField(null=True, upload_to='images')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.CharField(max_length=20, verbose_name='货号')),
                ('shape', models.CharField(max_length=10, verbose_name='形状')),
                ('weight', models.CharField(max_length=10, verbose_name='重量')),
                ('color', models.CharField(max_length=10, verbose_name='颜色')),
                ('neatness', models.CharField(max_length=10, verbose_name='净度')),
                ('cut', models.CharField(max_length=10, verbose_name='切工')),
                ('polish', models.CharField(max_length=10, verbose_name='抛光')),
                ('symmetry', models.CharField(max_length=10, verbose_name='对称')),
                ('fluorescence', models.CharField(max_length=10, verbose_name='荧光')),
                ('diameter', models.CharField(max_length=30, verbose_name='直径')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(max_length=200, verbose_name='邮箱')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
        ),
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eamil', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('datetime', models.CharField(max_length=30, null=True, verbose_name='出生日期')),
                ('telephone', models.CharField(max_length=20, null=True, verbose_name='电话')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='手机号')),
                ('qq', models.CharField(max_length=10, null=True, verbose_name='qq')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Product_detail'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
    ]