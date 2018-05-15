# -*- coding: utf-8 -*- 
#importacion de las clases
from openerp import api, fields, models 
from datetime import datetime 
#creamos la clase
class citasjsf(models.Model): 
#id de la clase
    _name = 'ej.citasjsf' 
 #atributos de nuestra clase
    autor = fields.Char(string='autor', required=True) 
 
    cita = fields.Text(string='cita', required=True) 
 
    fechaVisualizacion = fields.Datetime(string='fechaVisualizacion', required=True) 
 
    ordenVisualizacion = fields.Integer(string='ordenVisualizacion', required=True) 
 
