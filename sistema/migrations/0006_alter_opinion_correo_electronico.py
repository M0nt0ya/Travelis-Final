# Generated by Django 4.1 on 2022-08-14 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='correo_Electronico',
            field=models.CharField(max_length=100),
        ),
    ]
