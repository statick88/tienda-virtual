# Generated by Django 4.2.3 on 2023-07-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.IntegerField(choices=[('Cédula de identidad', 'Cédula de identidad'), ('RUC', 'RUC')]),
        ),
    ]