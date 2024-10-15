import math 
#clase creada para recibir informacion de el cuestionario y devolver el metodo de aprendizaje preferido por el alumno
#y la categoria de tiempo mas apropiada para el mismo
class EstimacionEstudio():

    #esta funcion se encarga de determinar el valor real de el tipo de contenido 
    #segun las preguntas del cuestionario, val1 y val2 son intercambiables.
    def ValoracionTipoContenido(val1,val2):
        vfinal=None
        if val1>val2:
            val2=(val2*10)/100
            vfinal=val2*val1
        else:
            val1=(val1*10)/100
            vfinal=val1*val2
        return vfinal

    # se encarga de determinar el valor "real" que puede el usuario estudiar segun el tiempo que 
    # dedica a consumir contenidos de sus hobby y a estudiar a voluntad
    def ValoracionTiempoEstudio(TiempoEstudio1,TiempoEstudio2):
        vfinal=None
        # obtenemos la diferencia entre los tiempos de estudio, se usa el valor absoluto
        dist_valores=abs(TiempoEstudio1-TiempoEstudio2)

        # identificamos el valor mas alto y le restamos 1 unidad para hacer que el valor final
        # sea mas cercano a un valor real 
        if TiempoEstudio1>TiempoEstudio2:
            TiempoEstudio1=TiempoEstudio1-1
        else:
            TiempoEstudio2=TiempoEstudio2-1
        
        # se calcula el valor final al obtener el promedio de los tiempos de estudio,
        # y se resta una fraccion de modo que se aproxime lo mas posible al valor apropiado  
        vfinal=((TiempoEstudio2+TiempoEstudio1)/2)-(dist_valores*0.2)
        
        return math.floor(vfinal)


    #se usa para identificar los valores que corresponden a las preferencias de la persona,recibe un objeto
    #con la informacion de las preguntas del contenido para encontrar la correcta devuelve una lista de contenido
    def PreferenciasContenido(self,obj):
        texto=self.ValoracionTipoContenido(obj.q1,obj.q5)
        audio=self.ValoracionTipoContenido(obj.q2,obj.q6)
        video=self.ValoracionTipoContenido(obj.q3,obj.q7)
    
        values=[texto,audio,video]
        return values

    
    #se usa para identificar los valores correspondientes a el tiempo de estudio de la persona
    def PreferenciasTiempo(self,obj):
        tiempo=self.ValoracionTiempoEstudio(obj.q4,obj.q8)
        return tiempo

    #se usa para verificar que el contenido si sea el correcto, recibe un objeto usuario
    #y el objeto contenido, devuelve true o false para cominucar si es valido o ono
    def VerificacionContenido(curso, usuario):
        Valido = True

        # Acceder a las preferencias de tipo de contenido del usuario
        PreferenciaAudio = usuario.preferenciaAudio  # Acceso correcto al atributo
        PreferenciaVideo = usuario.preferenciaVideo
        preferenciaTexto = usuario.preferenciaTexto

        categoria_curso = curso.tipoDeContenido

        # Lógica para verificar el tipo de contenido
        if (PreferenciaAudio >= PreferenciaVideo) and (PreferenciaAudio >= preferenciaTexto):
            if categoria_curso == 2:
                return Valido
            else:
                Valido = False
        elif (PreferenciaVideo >= PreferenciaAudio) and (PreferenciaVideo >= preferenciaTexto):
            if categoria_curso == 3:
                return Valido
        else:
            if categoria_curso == 1:
                return Valido

        Valido = False
        return Valido


    #se usa para verificar que la duracion de el contenido si sea el correcto, recibe un objeto usuario
    #y el objeto contenido, devuelve true o false para cominucar si es valido o ono
        
    def VerificacionTiempo(curso,usuario):
        duracion= curso.duracion
        duracion_predilecta= usuario.tiempoAprendizaje
        Valido=True

        if duracion == duracion_predilecta:
            return Valido

        else:
            valido=False
            return Valido
        

 