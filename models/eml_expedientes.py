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
	buque_id = fields.Many2one('eml.buques', string='Buque')
	travel_id = fields.Char(string='Número de Viaje')
	internal_ref = fields.Char(string='Ref. Interna')
	external_ref = fields.Char(string='Ref. Externa')
	containers_line = fields.Many2many('eml.containers')
	# account_move_lines = fields.One2many('account.move.line')

	# Counter Projects
	expedientes_count = fields.Integer(compute='_compute_project_count', string='Proyectos')
	facturas_count = fields.Integer(compute='_compute_invoice_count', string='Facturas')
	pagos_count = fields.Integer(compute='_compute_payment_count', string='Pagos')

	# Información Adicional
	project_id = fields.Many2one('project.project', string='Proyecto')
	account_analytic_id = fields.Many2one('account.analytic.account', string='Cuenta analítica')
	more_info = fields.Boolean(default=False)

	@api.model
	def create(self, vals):
		if not vals.get('note'):
			vals['note'] = 'Nuevo expediente'
			if vals.get('name', _('Nuevo expediente')) == _('Nuevo expediente'):
				vals['name'] = self.env['ir.sequence'].next_by_code('eml.expedientes.sequence') or _('Nuevo expediente')
				res = super(EMLExpedientes, self).create(vals)
				return res

	def action_create_project_analytic_account(self):
		vals = {
			'name': self.display_name,
			'partner_id': self.partner_id.id,
			'user_id': self.responsable_id.id,
			'date_start': self.start_date,
			'date': self.end_date,
			'analytic_account_id': self.account_analytic_id.id
		}
		self.env['project.project'].create(vals)
		vals = {
			'name': self.display_name,
			'partner_id': self.partner_id.id,
		}
		self.env['account.analytic.account'].create(vals)
		msj = "<b>¡Se ha creado un proyecto y una cuenta analítica!</b>"
		self.message_post(body=msj)
		for rec in self:
			rec.more_info = True

	def _compute_invoice_count(self):
		for rec in self:
			invoice_count = self.env['account.move.line'].search_count(['&', ('partner_id', '=', self.partner_id.id), ('analytic_account_id', '=', self.account_analytic_id.id), ('parent_state', '!=', 'draft')])
			rec.facturas_count = invoice_count

	def action_view_invoices(self):
		return {
			'type': 'ir.actions.act_window',
			'name': 'Facturas',
			'res_model': 'account.move.line',
			'domain': ['&', ('partner_id', '=', self.partner_id.id), ('analytic_account_id', '=', self.account_analytic_id.id), ('parent_state', '!=', 'draft')],
			'view_mode': 'tree,form',
			'target': 'current',
		}

	def _compute_project_count(self):
		for rec in self:
			invoice_count = self.env['project.project'].search_count([('partner_id', '=', rec.partner_id.id)])
			rec.expedientes_count = invoice_count

	def action_view_projects(self):
		return {
			'type': 'ir.actions.act_window',
			'name': 'Proyectos',
			'res_model': 'project.project',
			'domain': [('partner_id', '=', self.partner_id.id)],
			'view_mode': 'tree,form',
			'target': 'current',
		}

	def _compute_payment_count(self):
		for rec in self:
			payment_count = self.env['account.payment'].search_count([('partner_id', '=', rec.partner_id.id)])
			rec.pagos_count = payment_count

	def action_view_payments(self):
		return {
			'type': 'ir.actions.act_window',
			'name': 'Pagos',
			'res_model': 'account.payment',
			'domain': [('partner_id', '=', self.partner_id.id)],
			'view_mode': 'tree,form',
			'target': 'current',
		}
