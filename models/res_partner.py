# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Odoo.sh  odoo-bin -u em_logimpex --stop-after-init
# Pycham -c odoo.conf -d devd15 -u em_logimpex

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    bank_last_update = fields.Datetime(string='Última Revisión', default=fields.Datetime.now)
    bank_last_update_by = fields.Many2one('res.users', string='Revisado por', default=lambda self: self.env.user.id)
