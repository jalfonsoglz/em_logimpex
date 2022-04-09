# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class EMLBorders(models.Model):
    _inherit = ['mail.thread']
    _name = 'eml.borders'
    _description = 'Configurar Fronteras'
    _rec_name = 'name'
    _order = 'name'

    active = fields.Boolean(string='Activo', default=True, tracking=True)
    name = fields.Char(string='Nombre', required=True, tracking=True)
    country = fields.Many2one('res.country', string='País', required=True, tracking=True)
    note = fields.Text(string='Descripción', copy=False, tracking=True)

