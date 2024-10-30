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
        'Historia del arte en la Edad Media',
        'Introducción a la filosofía griega',
        'Cálculo diferencial para principiantes',
        'Fotografía creativa: técnicas y estilos',
        'Introducción a la biología molecular',
        'Técnicas de meditación y mindfulness',
        'Historia de las civilizaciones antiguas',
        'Psicología cognitiva aplicada',
        'Economía básica: oferta y demanda',
        'Introducción a la geopolítica contemporánea',
        'Técnicas de escritura creativa',
        'Astronomía: exploración del sistema solar',
        'Nutrición y salud: principios básicos',
        'Arquitectura moderna: tendencias y estilos',
        'Sociología de la globalización',
        'Desarrollo de habilidades de liderazgo',
        'Gestión del tiempo y productividad',
        'Música clásica: historia y compositores',
        'Introducción a la antropología cultural',
        'Técnicas de comunicación efectiva',
        'Educación ambiental y sostenibilidad',
        'Filosofía del lenguaje y semántica',
        'Gestión de proyectos para principiantes',
        'Introducción al marketing digital',
        'Exploración de la inteligencia emocional',
        'Historia del cine: orígenes y evolución',
        'Introducción a la botánica',
        'Principios de física cuántica',
        'Teoría de juegos aplicada',
        'Cultura y sociedad en la antigua Roma',
        'Fundamentos de la lógica matemática',
        'Introducción a la psicología del deporte',
        'Historia de la música popular',
        'Principios de química orgánica',
        'Introducción a la ingeniería genética',
        'Técnicas avanzadas de debate',
        'Sociología de la familia',
        'Biografía de grandes filósofos',
        'Geografía física y humana',
        'Introducción al urbanismo y planificación',
        'Técnicas de análisis literario',
        'La revolución industrial: causas y consecuencias',
        'Estudios de género y feminismo',
        'Microbiología y enfermedades infecciosas',
        'Principios de la ética profesional',
        'Ecología y conservación de ecosistemas',
        'Historia del Renacimiento europeo',
        'Introducción al teatro clásico',
        'Literatura universal: autores esenciales',
        'Neurociencia cognitiva: bases del comportamiento',
        'La evolución de los derechos humanos',
        'Cultura popular y medios de comunicación',
        'Introducción a la economía del comportamiento',
        'Antropología forense: métodos y casos',
        'Principios de la genética y evolución',
        'Introducción a la criptografía',
        'Mitos y leyendas en la antigüedad',
        'Desarrollo de la inteligencia artificial',
        'Historia de las religiones comparadas',
        'Estrategias de resolución de conflictos',
        'Cuidado de la salud mental: autocuidado y terapias',
        'Geología y formación de la Tierra',
        'Historia de la fotografía documental',
        'Técnicas de oratoria y persuasión',
        'Estadística aplicada: conceptos básicos',
        'Introducción a la nanotecnología',
        'Estudios culturales y postcolonialismo',
        'El arte de la improvisación musical',
        'Derecho internacional y diplomacia',
        'Fundamentos de la microbiología marina'
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
