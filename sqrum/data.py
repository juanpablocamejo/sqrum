# -*- coding: utf-8 -*-
from api.models import *
from datetime import date
desarrolladores = [
    Desarrollador(u'Juan Pablo'),
    Desarrollador(u'Fernando'),
    Desarrollador(u'Nicolas'),
    Desarrollador(u'Sergio'),
    Desarrollador(u'Fabrizio')
]
r1 = Rol(u"Desarrollador")
r2 = Rol(u"Product Owner")
r3 = Rol(u"Scrum Master")
roles = [r1,r2]
stories = [
    UserStory(r1, u'Agregar una User Story', para=u'Agregar funcionalidad al sistema', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r1, u'Ver la lista de user stories del product backlog', para=u'Tener a la vista todas las funcionalidades del proyecto', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r2, u'Cambiar el estado a una user story', para=u'Registrar lo que hago como desarrollador y que sea visible al resto del equipo', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r1, u'Visualizar un gráfico burn down de la iteración', para=u'Tener una visión de las tareas pendientes del sprint', obs=u'Observaciones', prioridad=1, estimacion=2),
    UserStory(r3, u'Cargar la estimación de una user story', para=u'mantener visible el esfuerzo que implica cada story en el tablero', obs=u'Observaciones', prioridad=1, estimacion=2)
]
iteraciones= [
    Iteracion(date(2016,1,1),date(2016,1,14))
    ]