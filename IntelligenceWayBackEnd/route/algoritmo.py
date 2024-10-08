from .models import ContenidoEducacion,formularioAprendizajeUsuario   # Importa el modelo
import math
class Ruta():

    def valorReal_materiales(val1,val2):
        vfinal=None
        if val1>val2:
            val2=(val2*10)/100
            vfinal=val2*val1
        else:
            val1=(val1*10)/100
            vfinal=val1*val2
        return vfinal
    
    def valorReal_tiempo(val1,val2):
        vfinal=None
        dist_valores=abs(val1-val2)

        if val1>val2:
            val1=val1-1
        else:
            val2=val2-1
        vfinal=((val2+val1)/2)-(dist_valores*0.2)
        
        return math.floor(vfinal)
    

    def preferencias_ContenidoEducacion (self,UserId):
        #se obtiene el ofrmulario relacionado al Usuario
        respuestas=formularioAprendizajeUsuario.objects.filter(usuario=UserId)
        #se obtienen los valores de las preguntas
        texto=self.valorReal_materiales(respuestas.q1,respuestas.q5)
        audio=self.valorReal_materiales(respuestas.q2,respuestas.q6)
        videos=self.valorReal_materiales(respuestas.q3,respuestas.q7)
        #se añaden estos valores a una lista
        values=[videos,texto,audio]
        #se devuelven estos valores de la lista
        return values

    def duracionContenido(self,UserId):
        #se obtiene el ofrmulario relacionado al Usuario
        respuestas=formularioAprendizajeUsuario.objects.filter(usuario=UserId)
        #se obtienen los valores de las preguntas
        tiempo=self.valorReal_tiempo(respuestas.q4,respuestas.q8)
        return 
         

    def checkPreferencias(self,IdCurso,userID):
        valido=True
        #obtenemos el valor preferido por el usuario
        preferenciascontenido=self.preferencias_ContenidoEducacion(userID)
        #se obtiene el contenido con el valor mas alto
        contenidopreferido=preferenciascontenido.index(max(preferenciascontenido))
        #se obtiene el contenido especifico
        contenido=ContenidoEducacion.objects.filter(idCurso=IdCurso)
       #---------------------------------------------------------------
        #se verifica que el tipo de contenido sea el apropiado, de no ser el correcto
        #devuelve falso
        if contenidopreferido == 0:
            #confirma el tipo de contenido
            if contenido.tipo_recurso!="video":
                #si no es el correcto devuelve falso
                valido=False
                return valido
            else:
                #si es el correcto se pasa a la siguiente instruccion
                pass
        elif contenidopreferido == 1:
            if contenido.tipo_recurso!="texto":
                valido=False
                return valido
            else:
                #si es el correcto se pasa a la siguiente instruccion
                pass
        elif contenidopreferido == 2:
            if contenido.tipo_recurso!="audio":
                valido=False
                return valido
            else:
                #si es el correcto se pasa a la siguiente instruccion
                pass
        else:
            pass
        #----------------------------------------
        #se verifica la duracion de el contenido para el usuario
        duracion=self.duracionContenido(userID)
        #se obtiene la duracion de el contenido
        contenidoduracion=contenido.duracion
        #se verifica que los valores sean los mismos 
        if contenidoduracion!=duracion:
                valido=False
                return valido
        else:
            pass

        return valido

    def obtener_contenidos_por_interes(self,tipo_interes,userID):

        ()
        #filtra contenido por tipo de interes
        contenido=ContenidoEducacion.objects.filter(tipo_interes=tipo_interes)
        #crear ruta de aprendizaje
        RutaAprendizaje= []
        #añadir a la ruta de aprendizaje el contenido que es valido segun las preferencias de la encuesta
        for i in contenido:
            if self.checkPreferencias(i.idCurso,userID):
                RutaAprendizaje.insert(i)
            else:
                pass
        return RutaAprendizaje
