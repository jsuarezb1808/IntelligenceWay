# Generated by Django 5.1.1 on 2024-10-15 22:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0008_alter_contenido_contenidosprevios'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.ManyToManyField(blank=True, to='route.rutaaprendizaje')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=255)),
                ('IdContenido', models.ForeignKey(default='Usuario borrado', on_delete=django.db.models.deletion.SET_DEFAULT, to='route.contenido')),
            ],
        ),
    ]
