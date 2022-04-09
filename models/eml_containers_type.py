# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EMLContainersType(models.Model):
    _inherit = ['mail.thread']
    _name = 'eml.containers.type'
    _description = 'Configurar Tipos de Contenedores'
    _rec_name = 'name'
    _order = 'name'

    active = fields.Boolean(string='Activo', default=True)
    name = fields.Char(string='Nombre', required=True)
    size = fields.Integer(string='Tamaño', required=True)
    code = fields.Text(string='Código', copy=False, required=True)
    teu = fields.Float(string="Monto de TEU", copy=False, required=True)
    note = fields.Text(string='Descripción', copy=False)
