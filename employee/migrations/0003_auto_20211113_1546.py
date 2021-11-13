# Generated by Django 3.2.9 on 2021-11-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employeemodel_staf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='gender',
            field=models.CharField(choices=[('2', 'Female'), ('1', 'Male')], default=1, max_length=15),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='staf',
            field=models.CharField(choices=[('3', 'Percobaan'), ('2', 'Kontrak'), ('3', 'Harian'), ('1', 'Tetap')], max_length=15),
        ),
    ]
