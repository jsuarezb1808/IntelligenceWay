from django.core.management.base import BaseCommand
from route.models import Contenido, Tag, Autor
import random

class Command(BaseCommand):
    help = 'Genera 100 contenidos para cada tag en la base de datos'

    def handle(self, *args, **kwargs):
        # Obtener todos los tags disponibles en la base de datos
        all_tags = Tag.objects.all()
        autor_obj = Autor.objects.first()  # Usa un autor existente o ajusta según tu lógica

        if not autor_obj:
            self.stdout.write(self.style.ERROR("No se encontró ningún autor en la base de datos."))
            return

        for tag in all_tags:
            self.stdout.write(f"Generando contenidos para el tag: {tag.tagName}")

            contenido_data = [
                {
                    'title': f"{tag.tagName} - Contenido {i+1}",
                    'autor': autor_obj,
                    'tags': [tag],
                    'duracion': random.randint(20, 200),
                    'tipoDeContenido': random.choice([1, 2, 3]),
                    'link': f"https://example.com/{tag.tagName.lower()}-contenido-{i+1}",
                    'description': f"Descripción del contenido de {tag.tagName} número {i+1}.",
                    'nivel': random.randint(1, 8)
                } 
                for i in range(100)
            ]

            # Creando los contenidos en la base de datos
            for contenido_info in contenido_data:
                contenido = Contenido.objects.create(
                    title=contenido_info['title'],
                    autor=contenido_info['autor'],
                    duracion=contenido_info['duracion'],
                    tipoDeContenido=contenido_info['tipoDeContenido'],
                    link=contenido_info['link'],
                    description=contenido_info['description'],
                    nivel=contenido_info['nivel']
                )
                contenido.tags.set(contenido_info['tags'])

            self.stdout.write(self.style.SUCCESS(f"100 contenidos generados para el tag: {tag.tagName}"))
