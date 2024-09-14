from models import ContenidoEducacion  # Importa el modelo

def obtener_contenidos_por_interes(tipo_interes):
    """
    Obtiene una lista de contenidos cuyo tipo de interés coincide con el valor dado.
    
    :param tipo_interes: El tipo de interés que deseas filtrar (e.g., 'python', 'java', 'django')
    :return: Lista de objetos ContenidoEducacion que coincidan con el tipo de interés
    """
    return ContenidoEducacion.objects.filter(tipo_interes=tipo_interes)
