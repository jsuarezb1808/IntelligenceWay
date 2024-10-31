import math 
# Class created to receive information from the questionnaire and return the preferred learning method of the student
# and the most appropriate time category for them

# This function is responsible for determining the real value of the type of content 
# according to the questions from the questionnaire; val1 and val2 are interchangeable.
def ValoracionTipoContenido(val1, val2):
    vfinal = None
    if val1 > val2:
        val2 = (val2 * 10) / 100
        vfinal = val2 * val1
    else:
        val1 = (val1 * 10) / 100
        vfinal = val1 * val2
    return vfinal

# Responsible for determining the "real" value that the user can study based on the time they 
# spend consuming content of their hobby and studying voluntarily
def ValoracionTiempoEstudio(TiempoEstudio1, TiempoEstudio2):
    vfinal = None
    # Obtain the difference between the study times; the absolute value is used
    dist_valores = abs(TiempoEstudio1 - TiempoEstudio2)
    # Identify the highest value and subtract 1 unit to make the final value
    # closer to a real value 
    if TiempoEstudio1 > TiempoEstudio2:
        TiempoEstudio1 = TiempoEstudio1 - 1
    else:
        TiempoEstudio2 = TiempoEstudio2 - 1
    
    # Calculate the final value by obtaining the average of the study times,
    # and subtract a fraction to approximate the appropriate value as closely as possible  
    vfinal = ((TiempoEstudio2 + TiempoEstudio1) / 2) - (dist_valores * 0.2)
    
    return math.floor(vfinal)

# Used to identify the values corresponding to the person's preferences; receives an object
# with the information from the content questions to find the correct one and returns a list of content
def PreferenciasContenido(obj):
    texto = ValoracionTipoContenido(obj.q1, obj.q5)
    audio = ValoracionTipoContenido(obj.q2, obj.q6)
    video = ValoracionTipoContenido(obj.q3, obj.q7)

    values = [texto, audio, video]
    return values

# Used to identify the values corresponding to the person's study time
def PreferenciasTiempo(obj):
    tiempo = ValoracionTiempoEstudio(obj.q4, obj.q8)
    return tiempo
    
# Used to verify that the content is correct; receives a user object
# and the content object, returns true or false to indicate if it is valid or not
def VerificacionContenido(curso, usuario):
    Valido = True

    # Access the user's content type preferences
    PreferenciaAudio = usuario.preferenciaAudio  # Correct access to the attribute
    PreferenciaVideo = usuario.preferenciaVideo
    preferenciaTexto = usuario.preferenciaTexto
    categoria_curso = curso.tipoDeContenido
    # Logic to verify the type of content
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

# Used to verify that the duration of the content is correct; receives a user object
# and the content object, returns true or false to indicate if it is valid or not
def VerificacionTiempo(curso, usuario):
    duracion = curso.duracion
    duracion_predilecta = usuario.tiempoAprendizaje
    print(duracion)
    # Mapear la duración de acuerdo a la preferencia
    if (duracion < 30 and duracion_predilecta == 1) or \
       (30 <= duracion < 60 and duracion_predilecta in [2, 3]) or \
       (90 <= duracion < 120 and duracion_predilecta in [4, 5]):
        return True

    return False
