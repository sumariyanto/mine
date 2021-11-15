# Generated by Django 3.2.9 on 2021-11-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_alter_contact_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='role',
            field=models.CharField(choices=[('1', 'Read'), ('3', 'Full'), ('2', 'ReadWrite')], default=1, max_length=15),
        ),
    ]