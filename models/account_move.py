# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields


class AccountMoveInherit(models.Model):
    _inherit = ['account.move']

    eml_folio_fact = fields.Char(string='Folio')
    eml_aprobado = fields.Boolean(string='Aprobado')
    eml_recepcion_conta = fields.Date(string='Fecha Recepción Contabilidad')
    eml_expediente = fields.Many2one('eml.expedientes', string='Expediente relacionado')
