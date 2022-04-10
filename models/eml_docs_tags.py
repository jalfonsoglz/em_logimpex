from odoo import fields, models, api


class EMLDocsTags(models.Model):
	_name = 'eml.docs.tags'
	_description = 'Etiquetado de Documentos'

	name = fields.Char()
	color = fields.Integer()
