# Generated by Django 4.1 on 2022-08-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_destino'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo_Electronico', models.CharField(max_length=100, unique=True)),
                ('opinion', models.CharField(max_length=5000)),
            ],
        ),
    ]
