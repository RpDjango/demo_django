# Generated by Django 4.1.7 on 2023-03-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='product_active',
            field=models.BooleanField(default=True),
        ),
    ]
