# -*- coding: utf-8 -*-
# Part of Odoo. Tutorials.

from odoo import fields, models, Command
from odoo.exceptions import UserError, ValidationError
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


class EstateInstallment(models.TransientModel):
    _name = 'estate.property.installment'
    _description = "Sell the property in installments"

    def _get_product(self):
        product_id = self.env['ir.config_parameter'].sudo().get_param('estate.default_admission_product_id')
        if product_id:
            return product_id
        else:
            raise ValidationError(
                "Please Choose Product in setting for Administrative fees"

            )

    fees_amount = fields.Float('Fees Amount', )
    installment_no = fields.Selection([('1', 'immediate'), ('6', '6 Months'), ('12', '12 Months'), ('24', '24 Months')],
                                      default='6')

    def insta_pay(self):
        props = self.env['estate.property'].browse(
            self.env.context.get('active_ids') if self.env.context.get('active_ids') else [])
        journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
        invoice = self.env["account.move"]
        # Another way to get the journal:
        # journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
        for prop in props:
            price = 0
            n = 0
            if self.installment_no == '1':
                print('0')
                n = 1
                price = prop.selling_price
            if self.installment_no == '6':
                print('6')
                n = 6
                price = prop.selling_price / 6
            if self.installment_no == '12':
                print('12')
                n = 12
                price = prop.selling_price / 12
            if self.installment_no == '24':
                print('24')
                n = 24
                price = prop.selling_price / 24
            vals1 = {
                "partner_id": prop.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
                "invoice_date": date.today(),
                "invoice_line_ids": [
                    Command.create({
                        "name": prop.name,
                        'product_id': prop.property_type_id.product_id.id,
                        "quantity": 1.0,
                        "price_unit": price,
                    }),
                    Command.create({
                        "name": "Administrative fees",
                        'product_id': self._get_product(),
                        "quantity": 1.0,
                        "price_unit": self.fees_amount,
                    }),
                ],
            }

            for no in range(n):
                print('start on zero = ',no)
                if no == 0:
                    invoice.create(vals1)
                    vals1['invoice_line_ids'].pop(1)
                else:
                    vals1['invoice_date'] = date.today() + relativedelta(months=no)
                    invoice.create(vals1)
