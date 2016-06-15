# -*- coding: utf-8 -*-
from api.models import *

r1 = Rol("Desarrollador")
r2 = Rol("Product Owner")
r3 = Rol("Scrum Master")
roles = [r1,r2]
stories = [
    UserStory(r1, u'Agregar una User Story', para=u'Agregar funcionalidad al sistema', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r1, u'Ver la lista de user stories del product backlog', para=u'Tener a la vista todas las funcionalidades del proyecto', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r2, u'Cambiar el estado a una user story', para=u'Registrar lo que hago como desarrollador y que sea visible al resto del equipo', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r1, u'Visualizar un grafico burn down de la iteracion', para=u'Tener una vision de las tareas pendientes del sprint', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r3, u'Cargar la estimacion de una user story', para=u'mantener visible el esfuerzo que implica cada story en el tablero', obs=u'Observaciones', prioridad=1, estimacion=2)
]
