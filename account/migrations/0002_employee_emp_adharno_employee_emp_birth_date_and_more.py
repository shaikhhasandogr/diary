# Generated by Django 4.2.16 on 2024-10-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_adharno',
            field=models.CharField(blank=True, max_length=12, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_caste',
            field=models.CharField(choices=[('GEN', 'General'), ('OBC', 'Other Backward Class'), ('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe'), ('NT', 'Nomadic Tribe'), ('OTH', 'Other')], default='GEN', max_length=3),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_category',
            field=models.CharField(choices=[('SCI', 'Scientific'), ('TECH', 'Technical'), ('ADMN', 'Administration'), ('MTS', 'Skilled Supporting Staff')], default='SCI', max_length=4),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_dogr_joining_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_group',
            field=models.CharField(choices=[('A', 'A Group'), ('B', 'B Group'), ('C', 'C Group')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_icar_joining_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_left_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_panno',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]