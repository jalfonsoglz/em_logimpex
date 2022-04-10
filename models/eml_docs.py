from odoo import fields, models, api


class EMLDocs(models.Model):
	_name = 'eml.docs'
	_description = 'Gestión de Documentos'
	_rec_name = 'name'
	_order = 'name'

	name = fields.Char(string='Nombre', required=True)
	partner_id = fields.Many2one('res.partner', string='Cliente', required=True, index=True)
	document = fields.Binary(string='Documento', copy=False)
	document_filename = fields.Char(string='Nombre del documento', copy=False)
	document_tag = fields.Many2many('eml.docs.tags', string='Etiquetas', copy=False)
	note = fields.Text(string='Descripción', copy=False)
