from .models import ContenidoEducacion, formularioAprendizajeUsuario
import math

class Ruta:

    @staticmethod
    def valorReal_materiales(val1, val2):
        vfinal = None
        if val1 > val2:
            val2 = (val2 * 10) / 100
            vfinal = val2 * val1
        else:
            val1 = (val1 * 10) / 100
            vfinal = val1 * val2
        return vfinal

    @staticmethod
    def valorReal_tiempo(val1, val2):
        dist_valores = abs(val1 - val2)
        if val1 > val2:
            val1 -= 1
        else:
            val2 -= 1
        vfinal = ((val2 + val1) / 2) - (dist_valores * 0.2)
        return math.floor(vfinal)

    def preferencias_ContenidoEducacion(self, user):
        # Obtener el formulario relacionado al usuario
        respuestas = formularioAprendizajeUsuario.objects.filter(usuario=user).first()

        if respuestas:
            # Obtener los valores de las preguntas
            texto = self.valorReal_materiales(respuestas.q1, respuestas.q5)
            audio = self.valorReal_materiales(respuestas.q2, respuestas.q6)
            video = self.valorReal_materiales(respuestas.q3, respuestas.q7)

            # Añadir estos valores a una lista
            values = [video, texto, audio]

            # Devolver la lista de valores
            return values
        return []

    def duracionContenido(self, user):
        # Obtener el formulario relacionado al usuario
        respuestas = formularioAprendizajeUsuario.objects.filter(usuario=user).first()
        
        if respuestas:
            # Obtener los valores de las preguntas
            tiempo = self.valorReal_tiempo(respuestas.q4, respuestas.q8)
            return tiempo
        return None

    def checkPreferencias(self, contenido, user):
        # Obtener las preferencias del usuario
        preferenciascontenido = self.preferencias_ContenidoEducacion(user)

        if not preferenciascontenido:
            return False  # Si no hay preferencias, no es válido

        # Obtener el tipo de contenido preferido
        contenidopreferido = preferenciascontenido.index(max(preferenciascontenido))

        # Verificar que el tipo de contenido sea apropiado
        if contenidopreferido == 0 and contenido.tipo_recurso != "video":
            return False
        elif contenidopreferido == 1 and contenido.tipo_recurso != "texto":
            return False
        elif contenidopreferido == 2 and contenido.tipo_recurso != "audio":
            return False

        # Verificar la duración del contenido
        duracion_preferida = self.duracionContenido(user)
        if duracion_preferida is not None and contenido.duracion != duracion_preferida:
            return False

        return True

    def obtener_contenidos_por_interes(self, tipo_interes, user):
        # Filtrar contenido por tipo de interés
        contenidos = ContenidoEducacion.objects.filter(tipo_interes=tipo_interes)
        RutaAprendizaje = []

        # Añadir a la ruta de aprendizaje el contenido válido según las preferencias
        for contenido in contenidos:
            if self.checkPreferencias(contenido, user):
                RutaAprendizaje.append(contenido)

        return RutaAprendizaje
