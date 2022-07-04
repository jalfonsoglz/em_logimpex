# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EMLSeaportsAirports(models.Model):
	_inherit = ['mail.thread']
	_name = 'eml.seaports.airports'
	_description = 'Configurar Puertos Marítimos y Aeropuertos'
	_rec_name = 'code'
	_order = 'code'

	active = fields.Boolean(string='Activo', default=True, tracking=True)
	name = fields.Char(string='Nombre', required=True, help='Nombre a mostrar en el listado', tracking=True)
	code = fields.Char(string='Código', required=True, help='Código IATA o Abreviatura', copy=False, tracking=True)
	category = fields.Selection([
		('port', 'Puerto'),
		('airport', 'Aeropuerto')
	],  string='Tipo', required=True, tracking=True, help='Elegir el tipo origen o destino')
	country = fields.Many2one('res.country', string='País', required=True, tracking=True)
	note = fields.Text(string='Descripción', copy=False, tracking=True)

	def name_get(self):
		result = []
		for rec in self:
			name = '[' + rec.code + '] ' + rec.name
			result.append((rec.id, name))
		return result
