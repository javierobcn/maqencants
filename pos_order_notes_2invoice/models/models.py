# -*- coding: utf-8 -*-

from odoo import api, fields,models

class PosConfig(models.Model):
	_inherit = 'pos.config'
	invoice_note = fields.Boolean('Print notes on the invoice', default=True)

class PosOrder(models.Model):
	_inherit = 'pos.order'

	def _action_create_invoice_line(self, line=False, invoice_id=False):
		InvoiceLine = self.env['account.invoice.line']
		inv_name = line.product_id.name_get()[0][1] 
		if line.order_line_note:
			inv_name = inv_name + ' '  + line.order_line_note
		inv_line = {
		    'invoice_id': invoice_id,
		    'product_id': line.product_id.id,
		    'quantity': line.qty if self.amount_total >= 0 else -line.qty,
		    'account_analytic_id': self._prepare_analytic_account(line),
		    'name': inv_name,
		    
		}
		# Oldlin trick
		invoice_line = InvoiceLine.sudo().new(inv_line)
		invoice_line._onchange_product_id()
		invoice_line.invoice_line_tax_ids = invoice_line.invoice_line_tax_ids.filtered(lambda t: t.company_id.id == line.order_id.company_id.id).ids
		fiscal_position_id = line.order_id.fiscal_position_id
		if fiscal_position_id:
		    invoice_line.invoice_line_tax_ids = fiscal_position_id.map_tax(invoice_line.invoice_line_tax_ids, line.product_id, line.order_id.partner_id)
		invoice_line.invoice_line_tax_ids = invoice_line.invoice_line_tax_ids.ids
		# We convert a new id object back to a dictionary to write to
		# bridge between old and new api
		inv_line = invoice_line._convert_to_write({name: invoice_line[name] for name in invoice_line._cache})
		inv_line.update(price_unit=line.price_unit, discount=line.discount, name=inv_name)
		return InvoiceLine.sudo().create(inv_line)


# 
# 	@api.model
# 	def _order_fields(self,ui_order):
# 		fields_return = super(PosOrder,self)._order_fields(ui_order)
# 		fields_return.update({'note':ui_order.get('order_note','')})
# 		return fields_return

# class PosOrderLine(models.Model):
# 	_inherit = 'pos.order.line'
# 	order_line_note = fields.Text('Extra Comments')
# 
# 	@api.model
# 	def _order_line_fields(self, line, session_id=None):
# 		fields_return = super(PosOrderLine,self)._order_line_fields(line,session_id=None)
# 		fields_return[2].update({'order_line_note':line[2].get('order_line_note','')})
# 		return fields_return

