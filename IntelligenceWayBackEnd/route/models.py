from django.db import models

# Create your models here.

class Route(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title

#se usa para guardar las respuestas del usuario    
class LearningMethods(models.Model):
  #valores posibles para los forms 
  FRECUENCY=[
        (1,'Nunca'),
        (2,'proco frecuente'),
        (3,'normalmente no'),
        (4,'frecuentemente'),
        (5,'siempre'),
    ]
#datos guardados de las preguntas 
  
  Q1=models.IntegerField(
     choices=FRECUENCY
  )
  Q3=models.IntegerField(
     choices=FRECUENCY
  )
  Q4=models.IntegerField(
     choices=FRECUENCY
  )
  Q2=models.IntegerField(
     choices=FRECUENCY
  )
  Q5=models.IntegerField(
     choices=FRECUENCY
  )
  Q6=models.IntegerField(
     choices=FRECUENCY
  )
#preguntas no obligatorias, se les predefine un valor
#en caso de que el cliente elija no responder
  Q7=models.IntegerField(
    choices=FRECUENCY,
    default=1
  )
  Q8=models.IntegerField(
    choices=FRECUENCY,
    default=1
  )
  Q9=models.IntegerField(
    choices=FRECUENCY,
    default=1
  )
  Q10=models.IntegerField(
    choices=FRECUENCY,
    default=1
  )
  Q11=models.IntegerField(
    choices=FRECUENCY,
    default=1
  )
  Q12=models.IntegerField(
    choices=FRECUENCY,
    default=1
  )