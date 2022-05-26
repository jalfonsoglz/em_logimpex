# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields


class IncotermsCodeInherit(models.Model):
	_inherit = ['account.incoterms']

	def name_get(self):
		result = []
		for rec in self:
			name = '[' + rec.code + '] ' + rec.name
			result.append((rec.id, name))
		return result
