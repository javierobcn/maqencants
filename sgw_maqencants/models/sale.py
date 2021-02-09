from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    price_unit = fields.Float(
        "Unit Price",
        required=True,
        digits=2,
        default=0.0,
    )
