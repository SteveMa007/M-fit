# Generated by Django 2.2.12 on 2022-03-25 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryOrder',
            fields=[
                ('order_num', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='訂單編號')),
                ('ordername', models.CharField(max_length=20, null=True, verbose_name='帳號')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('total_amount', models.IntegerField(verbose_name='總金額')),
                ('addr', models.CharField(max_length=100, verbose_name='配送地址')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='購買日期')),
            ],
            options={
                'verbose_name_plural': '歷史訂單',
                'db_table': 'users_history_order',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='帳號')),
                ('userpwd', models.CharField(max_length=32, verbose_name='密碼')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='電子信箱')),
                ('phone', models.CharField(max_length=10, verbose_name='手機')),
                ('addr', models.CharField(default='--尚無設定地址--', max_length=100, verbose_name='地址')),
                ('amount', models.IntegerField(default=0, verbose_name='消費金額')),
                ('permission', models.CharField(choices=[('user', 'user'), ('vendor', 'vendor'), ('manager', 'manager')], default='user', max_length=7, verbose_name='權限')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='註冊日期')),
                ('upload_time', models.DateField(auto_now=True, verbose_name='更新日期')),
                ('active', models.BooleanField(default=1, verbose_name='是否使用')),
            ],
            options={
                'verbose_name_plural': '使用者資訊',
                'db_table': 'users_user_profile',
            },
        ),
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='公司')),
                ('company_num', models.CharField(max_length=8, verbose_name='統一編號')),
                ('contact_name', models.CharField(max_length=10, verbose_name='聯絡人')),
                ('contact_tel', models.CharField(max_length=20, verbose_name='公司電話')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='合作日期')),
                ('upload_time', models.DateField(auto_now=True, verbose_name='更新日期')),
                ('active', models.BooleanField(default=1, verbose_name='是否使用')),
                ('contactor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
            ],
            options={
                'verbose_name_plural': '廠商資訊',
                'db_table': 'users_vendor_profile',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50, verbose_name='訂購商品')),
                ('item_size', models.CharField(max_length=10, verbose_name='商品尺寸')),
                ('item_price', models.IntegerField(verbose_name='商品價格')),
                ('item_num', models.IntegerField(verbose_name='訂購數量')),
                ('order_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.HistoryOrder')),
            ],
            options={
                'verbose_name_plural': '訂單品項',
                'db_table': 'users_order_items',
            },
        ),
    ]