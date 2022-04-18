# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields


class ProjectProjectInherit(models.Model):
    _inherit = ['project.project']

    eml_expediente = fields.Many2one('eml.expedientes', string='Expediente')
