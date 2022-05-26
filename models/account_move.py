# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields, api


class AccountMoveInherit(models.Model):
    _inherit = ['account.move']

    eml_folio_fact = fields.Char(string='Folio', required=True, copy=False, readonly=True,
                       default=lambda self: _('Nuevo folio'))
    eml_aprobado = fields.Boolean(string='Aprobado')
    eml_recepcion_conta = fields.Date(string='Fecha Recepción Contabilidad')
    eml_expediente = fields.Many2one('eml.expedientes', string='Expediente relacionado')

    @api.model
    def create(self, vals):
        vals['eml_folio_fact'] = self.env['ir.sequence'].next_by_code('eml.control.proveedores.sequence')
        return super(AccountMoveInherit, self).create(vals)
