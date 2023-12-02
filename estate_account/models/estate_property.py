# -*- coding: utf-8 -*-

from odoo import models, Command
from odoo.exceptions import UserError, ValidationError



class EstateProperty(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "estate.property"

    # ------------------------------------------res config setting -------------------------------

    def _get_product(self):
        product_id = self.env['ir.config_parameter'].sudo().get_param('estate.default_admission_product_id')
        if product_id:
            return product_id
        else:
            raise ValidationError(
                "Please Choose Product in setting for Administrative fees"

            )


    # ---------------------------------------- Action Methods -------------------------------------



    def action_sold(self):
        res = super().action_sold()
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        # Another way to get the journal:
        # journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
        for prop in self:
            self.env["account.move"].create(
                {
                    "partner_id": prop.buyer_id.id,
                    "move_type": "out_invoice",
                    "journal_id": journal.id,
                    "invoice_line_ids": [
                        Command.create({
                            "name": prop.name,
                            'product_id': prop.property_type_id.product_id.id,
                            "quantity": 1.0,
                            "price_unit": prop.selling_price,
                        }),
                        Command.create({
                            "name": "Administrative fees",
                            'product_id': self._get_product(),
                            "quantity": 1.0,
                            "price_unit": 100.0,
                        }),
                    ],
                }
            )
        return res
