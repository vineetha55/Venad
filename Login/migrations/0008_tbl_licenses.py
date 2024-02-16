# Generated by Django 5.0.2 on 2024-02-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_tbl_bank_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_licenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_name', models.CharField(max_length=100, null=True)),
                ('license_number', models.CharField(max_length=100, null=True)),
                ('expiry_reminder', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('license_file', models.ImageField(null=True, upload_to='license')),
                ('status', models.BooleanField(default=True, null=True)),
                ('dt', models.DateField(auto_now_add=True)),
            ],
        ),
    ]