# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EMLOperationType(models.Model):
	_inherit = ['mail.thread']
	_name = 'eml.operation.type'
	_description = 'Configurar Tipos de Operación'
	_order = 'name'
	_rec_name = 'name'

	active = fields.Boolean(string='Activo', default=True, tracking=True)
	name = fields.Char(string='Nombre', required=True, tracking=True)
	category = fields.Selection([
		('CANJE', 'Canje'),
		('EXPCA', 'Expo Carga'),
		('EXPVE', 'Expo Vehículo'),
		('IMPCA', 'Impo Carga'),
		('IMPTE', 'Impo Temporal'),
		('MENAJ', 'Menaje'),
		('MUDLO', 'Mud Local'),
		('OPESP', 'Op Esp Mudanzas'),
		('RETCA', 'Ret Carga'),
		('SERLO', 'Serv Local')], string='Tipo', required=True, tracking=True, help='Elegir el tipo origen o destino')
	note = fields.Text(string='Descripción', tracking=True)
