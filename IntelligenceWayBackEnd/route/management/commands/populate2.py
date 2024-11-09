from django.core.management.base import BaseCommand
from ...models import Tag, Autor, Contenido
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data for Contenido'

    def handle(self, *args, **kwargs):
        # Get all existing authors and tags
        autores = Autor.objects.all()
        tags = Tag.objects.all()

        # Check that there are available authors and tags
        if not autores.exists() or not tags.exists():
            self.stdout.write(self.style.ERROR('No authors or tags available.'))
            return

        # Sample data for contents
        titles = [
        "Fundamentos de Machine Learning",
    "Principios de Bioética",
    "Microbiología Básica",
    "Blockchain y Aplicaciones Financieras",
    "Neurociencia para Principiantes",
    "Economía Circular y Sostenibilidad",
    "Desarrollo Sostenible y Medioambiente",
    "Introducción al Cambio Climático",
    "Energías Renovables y Eficiencia Energética",
    "Psicología Cognitiva Aplicada",
    "Filosofía Moderna y Contemporánea",
    "Historia de las Civilizaciones Antiguas",
    "Ética y Moral en la Sociedad Actual",
    "Programación Avanzada en Python",
    "Ciencia de Datos para Todos",
    "Astrofísica: Explorando el Universo",
    "Ciberseguridad y Protección de Datos",
    "Sistemas Operativos: Teoría y Práctica",
    "Introducción a Redes Neuronales",
    "Fundamentos de Marketing Digital",
    "Finanzas Corporativas para No Financieros",
    "Criptomonedas y Finanzas Descentralizadas",
    "Introducción a la Ingeniería de Software",
    "Diseño Gráfico: Principios y Técnicas",
    "Gestión de Proyectos con Metodologías Ágiles",
    "Big Data y Análisis de Datos Masivos",
    "Análisis Financiero para la Toma de Decisiones",
    "Introducción a la Sociología",
    "Química Orgánica Básica",
    "Biotecnología y su Impacto en la Sociedad",
    "Derecho Internacional Público y Privado",
    "Antropología Cultural y Diversidad",
    "Desarrollo de Videojuegos desde Cero",
    "Epidemiología y Salud Pública",
    "Introducción a la Robótica",
    "Nanotecnología y sus Aplicaciones",
    "Econometría Aplicada a la Economía",
    "Matemáticas Avanzadas para Científicos",
    "Investigación de Operaciones en Empresas",
    "Electrónica Básica y Circuitos",
    "Tecnologías Emergentes en la Industria",
    "Lingüística Aplicada y Comunicación",
    "Educación Especial e Inclusión",
    "Análisis de Algoritmos Computacionales",
    "Fotografía Digital: Técnicas y Composición",
    "Arquitectura de Redes y Comunicaciones",
    "Realidad Aumentada y Realidad Virtual",
    "Diseño UX/UI para Aplicaciones",
    "Desarrollo Web Full Stack",
    "Astronomía: Exploración del Cosmos",
    "Logística y Gestión de la Cadena de Suministro"
        ]

        # Create contents
        for title in titles:
            # Select a random author and set of tags
            autor = random.choice(autores)
            selected_tags = random.sample(list(tags), k=random.randint(1, 3))  # Select between 1 and 3 tags

            # Create content
            contenido = Contenido(
                title=title,
                autor=autor,
                duracion=random.randint(5, 120),  # Random duration between 5 and 120 minutes
                tipoDeContenido=random.randint(1, 3),  # Random content type (1, 2 or 3)
                link=f'https://example.com/{title.replace(" ", "-").lower()}',  # Example link
                description=f'This is a summary of {title}.',  # Simple description
            )
            contenido.save()  # Save the content to the database
            
            # Assign tags to the content
            contenido.tags.set(selected_tags)  # Assign random tags
            contenido.save()  # Save changes

            self.stdout.write(self.style.SUCCESS(f'Content "{title}" created successfully.'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
