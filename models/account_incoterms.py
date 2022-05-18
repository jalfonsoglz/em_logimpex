# -*- coding: utf-8 -*-

from odoo import models


class IncotermsCodeInherit(models.Model):
	_inherit = ['account.incoterms']

	def name_get(self):
		result = []
		for rec in self:
			name = '[' + rec.code + '] ' + rec.name
			result.append((rec.id, name))
		return result
