# Generated by Django 3.2.9 on 2021-11-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='staf',
            field=models.CharField(choices=[('2', 'Kontrak'), ('3', 'Percobaan'), ('3', 'Harian'), ('1', 'Tetap')], max_length=15),
        ),
    ]