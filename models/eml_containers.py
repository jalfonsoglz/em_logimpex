# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EMLContainers(models.Model):
    _inherit = ['mail.thread']
    _name = 'eml.containers'
    _description = 'Contenedores'
    _rec_name = 'name'
    _order = 'name'

    active = fields.Boolean(string='Activo', default=True)
    name = fields.Char(string='Nombre', required=True)
    containers_type = fields.Many2one('eml.containers.type',
                                      string='Tipo de Contenedor', required=True, tracking=True)
    condition = fields.Selection([
        ('FCL', 'FCL'), ('LCL', 'LCL'), ('FCL/LCL', 'FCL/LCL'), ('FTL', 'FTL'), ('LTL', 'LTL')
    ], string='Condición', required=True, tracking=True)
    weight = fields.Float(string='Peso (kg)', tracking=True)
    precinto = fields.Integer(string='Precinto', tracking=True)
    bultos = fields.Integer(string='Bultos', tracking=True)
    percent_usage = fields.Float(string='% de Uso', default="100", tracking=True)
    note = fields.Text(string='Descripción', tracking=True)
