# Generated by Django 5.0.2 on 2024-02-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_rename_basic_info_cmp_tbl_basic_info_cmp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_basic_info_cmp',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
