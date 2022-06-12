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
    fecha_pago = fields.Date(string='Fecha de Pago', default=fields.Date.today, required=True)
    num_proveedor = fields.Char(
        related='partner_id.ref', string='Número de Proveedor')
    account_type = fields.Char(string='Tipo de Cuenta')
    account_id = fields.Many2one(
        related='partner_id.property_account_receivable_id', string='Número de Cuenta Contable')
    partner_id = fields.Many2one('res.partner', string='Beneficiario')
    partner_id_vat = fields.Char(
        related='partner_id.vat', string='RFC')
    partner_id_accounts = fields.Many2one('res.partner.bank', string='Cuentas de Banco')
    partner_id_acc_bank = fields.Char(
        related='partner_id_accounts.bank_name', string='Banco', readonly=True)
    partner_id_acc_c_bank = fields.Char(
        related='partner_id_accounts.bank_id.l10n_mx_edi_code', string='Código', readonly=True)
    partner_id_acc_number = fields.Char(
        related='partner_id_accounts.acc_number', string='Número de cuenta', readonly=True)
    partner_id_acc_clabe = fields.Char(
        related='partner_id_accounts.l10n_mx_edi_clabe', string='CLABE', readonly=True)
    partner_id_acc_currency = fields.Many2one(
        related='partner_id_accounts.currency_id', string='Moneda de la Cuenta', readonly=True)
    monto = fields.Monetary(string='Monto')
    currency_id = fields.Many2one('res.currency', string='Moneda')
    forma_pago_id = fields.Many2one('account.move', string='Forma de Pago')
    anticipo = fields.Boolean(string='Anticipo', default=False)
    anticipo_monto = fields.Monetary(string='Monto del Anticipo')
    anticipo_currency_id = fields.Many2one('res.currency', string='Moneda del Anticipo')
    concept = fields.Text(string='Concepto')
    eml_expediente = fields.Many2one('eml.expedientes', string='Expediente')
    country_id = fields.Many2one(
        related='partner_id.country_id', string='País')
    partner_id_email = fields.Char(
        related='partner_id.email', string='Email')
    solicitante_id = fields.Many2one('res.users', string='Solicitante', default=lambda self: self.env.user)
    auth_user1 = fields.Many2one('res.users', string='Autorización Nivel 1')
    auth_user2 = fields.Many2one('res.users', string='Autorización Nivel 2')
    auth_check1 = fields.Boolean(default=False)
    auth_check2 = fields.Boolean(default=False)

    @api.model
    def create(self, vals):
        vals['solicitud'] = self.env['ir.sequence'].next_by_code('eml.transferencias.sequence')
        res = super(EMLTransferencia, self).create(vals)
        return res
