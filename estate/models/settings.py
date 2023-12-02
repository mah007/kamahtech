#settings
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    add_fee_default_product_id = fields.Many2one(
        'product.product',
        'admission fee Product',
        domain="[('type', '=', 'service')]",
        config_parameter='estate.default_admission_product_id',
        help='Default product used for payment admission')




