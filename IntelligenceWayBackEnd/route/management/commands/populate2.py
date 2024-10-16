from django.core.management.base import BaseCommand
from ...models import Tag, Autor, Contenido
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data for Contenido'

    def handle(self, *args, **kwargs):
        # Obtener todos los autores y tags existentes
        autores = Autor.objects.all()
        tags = Tag.objects.all()

        # Verificar que haya autores y tags disponibles
        if not autores.exists() or not tags.exists():
            self.stdout.write(self.style.ERROR('No hay autores o tags disponibles.'))
            return

        # Datos de ejemplo para contenidos
        titles = [
            'Aprendiendo Django desde cero',
            'Introducción a la inteligencia artificial',
            'Cómo crear APIs RESTful con Django',
            'Desarrollo web con Python',
            'Machine Learning para principiantes',
            'Optimización de consultas en bases de datos',
            'Frameworks de JavaScript populares',
            'Principios de diseño de software',
            'Seguridad en aplicaciones web',
            'Introducción a Docker y contenedores'
        ]

        # Crear contenidos
        for title in titles:
            # Seleccionar un autor y un conjunto de tags aleatorios
            autor = random.choice(autores)
            selected_tags = random.sample(list(tags), k=random.randint(1, 3))  # Seleccionar entre 1 y 3 tags

            # Crear el contenido
            contenido = Contenido(
                title=title,
                autor=autor,
                duracion=random.randint(5, 120),  # Duración aleatoria entre 5 y 120 minutos
                tipoDeContenido=random.randint(1, 3),  # Tipo de contenido aleatorio (1, 2 o 3)
                link=f'https://example.com/{title.replace(" ", "-").lower()}',  # Enlace de ejemplo
                description=f'Este es un resumen de {title}.',  # Descripción simple
            )
            contenido.save()  # Guardar el contenido en la base de datos
            
            # Asignar tags al contenido
            contenido.tags.set(selected_tags)  # Asignar tags aleatorios
            contenido.save()  # Guardar los cambios

            self.stdout.write(self.style.SUCCESS(f'Contenido "{title}" creado exitosamente.'))

        self.stdout.write(self.style.SUCCESS('Base de datos poblada exitosamente.'))
