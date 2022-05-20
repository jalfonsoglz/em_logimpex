# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class EMLExpedientes(models.Model):
	_inherit = ['mail.thread']
	_name = 'eml.expedientes'
	_description = 'Expedientes'
	_rec_name = 'name'
	_order = 'name desc'

	# Información General del Expediente
	active = fields.Boolean(string='Activo', default=True)
	name = fields.Char(string='Nombre', required=True, copy=False, readonly=True,
	                   default=lambda self: _('Nuevo expediente'))
	operation_type = fields.Many2one('eml.operation.type', string='Tipo de Operación', required=True)
	service_type = fields.Selection([('load', 'Cargo'), ('moving', 'Mudanza')],
	                                string='Cargo / Mudanza', required=True)
	move_type = fields.Selection([('import', 'Importación'), ('export', 'Exportación'), ('national', 'Nacional')],
	                             string='Imp / Exp / Nac', required=True)
	transportation_type = fields.Selection([('marine', 'Marítimo'), ('air', 'Aéreo'), ('ground', 'Terrestre')],
	                                       string='Marítimo / Aéreo / Terrestre', required=True)
	transportation_border = fields.Many2one('eml.borders', string='Frontera')

	# Información de Peso Volumen
	volumen = fields.Float(string='Volumen (m³)')
	weight = fields.Float(string='Peso (kg)')
	weight_chargeable = fields.Float(string='Peso Cobrable (kg)')
	pza_num = fields.Integer(string='# de Piezas')
	amount = fields.Monetary(string='Valor')
	currency_id = fields.Many2one('res.currency', string='Moneda')
	note = fields.Text(string='Notas')

	# Información de Origen / Destino / Viaje
	origin = fields.Many2one('res.country', string='Origen', required=True)
	destiny = fields.Many2one('res.country', string='Destino', required=True)
	start_date = fields.Date(string='Fecha Est. Inicio', default=fields.Date.today, required=True)
	end_date = fields.Date(string='Fecha Est. Fin', default=fields.Date.today)
	partner_id = fields.Many2one('res.partner', string='Cliente')
	invoice_partner_id = fields.Many2one('res.partner', string='Cliente a Facturar')
	vendor_id = fields.Many2one('res.partner', string='Vendedor')
	agent_id = fields.Many2one('res.partner', string='Agente')
	agent_mx_id = fields.Many2one('res.partner', string='Agente en México')
	responsable_id = fields.Many2one('res.users', string='Responsable')

	# Información de Seguimiento
	ref = fields.Char(string='Referencia Interna')
	pickup = fields.Char(string='Recolección')
	load = fields.Many2one('eml.seaports.airports', string='Carga')
	unload = fields.Many2one('eml.seaports.airports', string='Descarga')
	delivery = fields.Char(string='Entrega')
	master = fields.Char(string='Master')
	house = fields.Char(string='House')
	incoterm_id = fields.Many2one('account.incoterms', string='Incoterms')
	fw_origen = fields.Char(string='FW Origen')
	fw_destino = fields.Char(string='FW Destino')
	mudancero_destino = fields.Char(string='Mudancero Destino')

	# Campos de Documentación del Embarque
	doc_embarque = fields.Binary(string="Documentos de Embarque")
	doc_factura_comercial = fields.Binary(string="Factura Comercial")
	doc_lista_empaque = fields.Binary(string="Lista de Empaque")
	doc_blawbbol = fields.Binary(string="BL / AWB / BOL")
	doc_cert_origen = fields.Binary(string="Certificado de Origen")
	doc_ficha_tecnica = fields.Binary(string="Ficha Técnica")

	# Líneas de Contenedores
	buque_id = fields.Char(string='Buque')
	travel_id = fields.Char(string='Número de Viaje')
	internal_ref = fields.Char(string='Referencia Interna')
	external_ref = fields.Char(string='Referencia Externa')
	containers_line = fields.Many2many('eml.containers')

	# Counter Projects
	expedientes_count = fields.Integer(compute='_compute_projects_count', string='Proyectos')

	@api.model
	def create(self, vals):
		if not vals.get('note'):
			vals['note'] = 'Nuevo expediente'
			if vals.get('name', _('Nuevo expediente')) == _('Nuevo expediente'):
				vals['name'] = self.env['ir.sequence'].next_by_code('eml.expedientes.sequence') or _('Nuevo expediente')
				res = super(EMLExpedientes, self).create(vals)
				return res
