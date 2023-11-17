# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	def action_create_invoice(self):
		''' Open the account.payment.register wizard to pay the selected journal entries.
		:return: An action opening the account.payment.register wizard.
		'''
		return {
			'name': _('Create invoices'),
			'res_model': 'sale.advance.payment.inv',
			'view_mode': 'form',
			'context': {
				'active_model': 'sale.order',
				'active_ids': self.ids,
			},
			'target': 'new',
			'type': 'ir.actions.act_window',
		}