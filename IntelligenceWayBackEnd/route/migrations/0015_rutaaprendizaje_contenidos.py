# Generated by Django 5.1.1 on 2024-10-31 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0014_remove_rutaaprendizaje_contenidos_progresocontenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutaaprendizaje',
            name='contenidos',
            field=models.ManyToManyField(related_name='rutas', through='route.ProgresoContenido', to='route.contenido'),
        ),
    ]