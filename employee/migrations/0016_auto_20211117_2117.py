# Generated by Django 3.2.9 on 2021-11-17 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20211117_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='bagian',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='employee.bagianmodel'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='golongan',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='employee.golonganmodel'),
        ),
    ]