# Generated by Django 2.2.12 on 2022-03-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220325_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyorder',
            name='paypal_id',
            field=models.CharField(default='FIRST TEST', max_length=255, verbose_name='PayPal訂單編號'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historyorder',
            name='status',
            field=models.BooleanField(default=0, verbose_name='訂單狀態'),
        ),
    ]