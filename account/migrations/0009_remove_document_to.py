# Generated by Django 4.2.16 on 2024-10-24 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_vendor_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='to',
        ),
    ]
