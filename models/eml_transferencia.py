# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class EMLTransferencia(models.Model):
    _inherit = ['mail.thread']
    _name = 'eml.transferencia'
    _description = 'Solicitud de Transferencias'
    _rec_name = 'solicitud'
    _order = 'solicitud'

    solicitud = fields.Char(string='Nombre', required=True, copy=False, readonly=True,
                       default=lambda self: _('Nueva solicitud de transferencia'))
    eml_expediente = fields.Many2one('eml.expedientes', string='Expediente')
    fecha_pago = fields.Date(string='Fecha de Pago', default=fields.Date.today, required=True)
    monto = fields.Monetary(string='Monto')
    currency_id = fields.Many2one('res.currency', string='Moneda')
    concept = fields.Text(string='Concepto')
    anticipo = fields.Boolean(string='Anticipo', default=False)
    anticipo_monto = fields.Monetary(string='Monto del Anticipo')
    anticipo_currency_id = fields.Many2one('res.currency', string='Moneda del Anticipo')
    solicitante_id = fields.Many2one('res.users', string='Solicitante')
    autorizacion1_id = fields.Many2one('res.users', string='Autorización Nivel 1')
    autorizacion2_id = fields.Many2one('res.users', string='Autorización Nivel 2')
    authorization1 = fields.Boolean(default=False)
    authorization2 = fields.Boolean(default=False)
