# Generated by Django 4.1.3 on 2024-06-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snip', '0006_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(default='price', max_length=20),
        ),
    ]