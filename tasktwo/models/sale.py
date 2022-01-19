# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    dimension = fields.Char(string='Dimension')

    def _prepare_procurement_values(self, group_id=False):
        print('-------------------------1')
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        res.update({'dimension': self.dimension})
        return res

    def _prepare_invoice_line(self, **vals):
        res = super(SaleOrderLine, self)._prepare_invoice_line(vals)
        res.update({'dimension': self.dimension})
        return res


class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values):
        res = super(StockRuleInherit, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id,
                                                                   name, origin, company_id, values)
        print('-------------------------2', values)
        res['dimension'] = values.get('dimension', False)
        return res


class StockMoveLine(models.Model):
    _inherit = "stock.move"

    dimension = fields.Char(string='Dimension')


class AccountInvoiceLine(models.Model):
    _inherit = "account.move.line"

    dimension = fields.Char(string='Dimension')
