# Generated by Django 5.0.2 on 2024-02-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('dt', models.DateField(auto_now_add=True, null=True)),
                ('tm', models.TimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]