# Generated by Django 4.0.5 on 2022-06-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id de la categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(max_length=50, verbose_name='Nombre de la categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
    ]
