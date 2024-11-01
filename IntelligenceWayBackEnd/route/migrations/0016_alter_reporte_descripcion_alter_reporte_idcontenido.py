# Generated by Django 5.1.1 on 2024-11-01 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0015_rutaaprendizaje_contenidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='descripcion',
            field=models.CharField(choices=[('gramatica_ortografia', 'Error de gramática o ortografía'), ('enlace_roto', 'Enlace roto'), ('error_formato', 'Error de formato'), ('imagen_video_no_visible', 'Imágenes o videos no visibles'), ('contenido_incorrecto', 'Error en el contenido'), ('problemas_audio', 'Problemas de audio'), ('problema_navegacion', 'Problema de navegación'), ('contenido_no_accesible', 'Contenido no accesible'), ('error_ejercicio', 'Error en ejercicios o cuestionarios'), ('tiempo_carga', 'Tiempo de carga lento'), ('compatibilidad', 'Problemas de compatibilidad'), ('error_traduccion', 'Error de traducción')], max_length=50),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='idContenido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='route.contenido'),
        ),
    ]
