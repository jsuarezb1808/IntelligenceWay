from django.core.management.base import BaseCommand
from ...models import Tag, Autor, Contenido
import random

class Command(BaseCommand):
    help = 'Poblar la base de datos con datos de prueba'

    def handle(self, *args, **kwargs):
        # Crear etiquetas
        tags = ['Educación', 'Tecnología', 'Ciencia', 'Historia', 'Matemáticas', 'Literatura', 'Arte', 'Salud']
        created_tags = [Tag.objects.create(tagName=tag) for tag in tags]

        # Crear autores
        autores_nombres = ['Juan Pérez', 'Ana López', 'Carlos Martínez', 'Laura Gómez', 'Pedro Fernández', 
                           'María Ruiz', 'Luis Castro', 'Elena Torres', 'Jorge Morales', 'Sofía Romero']
        created_autores = [Autor.objects.create(nombre=n) for n in autores_nombres]

        # Crear contenidos
        contenidos_data = [
            {
                'title': 'Introducción a la Programación',
                'autor': created_autores[0],
                'duracion': 60,
                'tipoDeContenido': 1,
                'link': 'https://ejemplo.com/intro-programacion',
                'description': 'Un curso básico sobre programación.',
                'tags': [created_tags[0], created_tags[1]]
            },
            {
                'title': 'Avances en Inteligencia Artificial',
                'autor': created_autores[1],
                'duracion': 90,
                'tipoDeContenido': 1,
                'link': 'https://ejemplo.com/ia-avances',
                'description': 'Un análisis de los últimos avances en IA.',
                'tags': [created_tags[1], created_tags[2]]
            },
            {
                'title': 'Historia de la Ciencia',
                'autor': created_autores[2],
                'duracion': 120,
                'tipoDeContenido': 2,
                'link': 'https://ejemplo.com/historia-ciencia',
                'description': 'Un recorrido por la historia de la ciencia.',
                'tags': [created_tags[0], created_tags[3]]
            },
            {
                'title': 'Teoría de Números',
                'autor': created_autores[3],
                'duracion': 45,
                'tipoDeContenido': 1,
                'link': 'https://ejemplo.com/teoria-numeros',
                'description': 'Explorando la teoría de números y sus aplicaciones.',
                'tags': [created_tags[4]]
            },
            {
                'title': 'Literatura Clásica',
                'autor': created_autores[4],
                'duracion': 80,
                'tipoDeContenido': 1,
                'link': 'https://ejemplo.com/literatura-clasica',
                'description': 'Un análisis de las obras clásicas de la literatura.',
                'tags': [created_tags[5]]
            },
            {
                'title': 'Arte Moderno',
                'autor': created_autores[5],
                'duracion': 70,
                'tipoDeContenido': 2,
                'link': 'https://ejemplo.com/arte-moderno',
                'description': 'Un vistazo al arte moderno y sus principales exponentes.',
                'tags': [created_tags[6], created_tags[1]]
            },
            {
                'title': 'Salud y Bienestar',
                'autor': created_autores[6],
                'duracion': 50,
                'tipoDeContenido': 1,
                'link': 'https://ejemplo.com/salud-bienestar',
                'description': 'Consejos y técnicas para un estilo de vida saludable.',
                'tags': [created_tags[7]]
            },
            {
                'title': 'Matemáticas para Todos',
                'autor': created_autores[7],
                'duracion': 55,
                'tipoDeContenido': 1,
                'link': 'https://ejemplo.com/matematicas-para-todos',
                'description': 'Aprende matemáticas de manera divertida y sencilla.',
                'tags': [created_tags[4], created_tags[0]]
            },
            {
                'title': 'Avances en Medicina',
                'autor': created_autores[8],
                'duracion': 100,
                'tipoDeContenido': 2,
                'link': 'https://ejemplo.com/avances-medicina',
                'description': 'Un resumen de los últimos avances en medicina.',
                'tags': [created_tags[3], created_tags[7]]
            },
            {
                'title': 'Desarrollo Personal',
                'autor': created_autores[9],
                'duracion': 65,
                'tipoDeContenido': 1,
                'link': 'https://ejemplo.com/desarrollo-personal',
                'description': 'Consejos para mejorar tu vida personal y profesional.',
                'tags': [created_tags[0], created_tags[5]]
            },
        ]

        created_contenidos = []
        for data in contenidos_data:
            contenido = Contenido.objects.create(
                title=data['title'],
                autor=data['autor'],
                duracion=data['duracion'],
                tipoDeContenido=data['tipoDeContenido'],
                link=data['link'],
                description=data['description'],
            )
            contenido.tags.set(data['tags'])
            created_contenidos.append(contenido)

        self.stdout.write(self.style.SUCCESS('Base de datos poblada con éxito!'))
