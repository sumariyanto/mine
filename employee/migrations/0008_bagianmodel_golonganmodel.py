# Generated by Django 3.2.9 on 2021-11-15 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employeemodel_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='BagianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bagian', models.CharField(max_length=50)),
                ('info', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='GolonganModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('golongan', models.CharField(max_length=25)),
                ('info', models.TextField(max_length=250)),
            ],
        ),
    ]
