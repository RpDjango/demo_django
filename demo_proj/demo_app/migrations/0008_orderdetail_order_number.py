# Generated by Django 4.1.4 on 2023-04-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0007_alter_cartdetail_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='order_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]