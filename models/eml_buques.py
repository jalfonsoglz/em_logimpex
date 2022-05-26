# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class EMLBuques(models.Model):
    _inherit = ['mail.thread']
    _name = 'eml.buques'
    _description = 'Configurar Buques'
    _rec_name = 'name'
    _order = 'name'

    active = fields.Boolean(string='Activo', default=True)
    name = fields.Char(string='Nombre', required=True)

