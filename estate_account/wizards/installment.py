# -*- coding: utf-8 -*-
# Part of Odoo. Tutorials.

from odoo import fields, models, Command
from odoo.exceptions import UserError, ValidationError
from datetime import date,timedelta
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
        # Another way to get the journal:
        # journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
        for prop in props:
            price = 0
            n = 0
            com =[]
            if self.installment_no == '1':
                price = prop.selling_price
                n  = 0
            elif self.installment_no == '6':
                n =5
                price = prop.selling_price/6
            elif self.installment_no == '12':
                n =11
                price = prop.selling_price/12
            elif self.installment_no == '24':
                n=23
                price = prop.selling_price/24

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
            valn = {
                "partner_id": prop.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
                # "invoice_date": date.today() ,
                "invoice_line_ids": [

                ],
            }
            if self.installment_no == '1':
                self.env["account.move"].create(vals1)
            elif self.installment_no == '6':
                item = Command.create({
                        "name": prop.name,
                        'product_id': prop.property_type_id.product_id.id,
                        "quantity": 1.0,
                        "price_unit": price,
                    }),
                valn['invoice_line_ids'].append(item)

                com.append(vals1)
                print('val1',vals1)
                print('valn',valn)
                for no in range(n):
                    vals1['invoice_date'] = date.today() + relativedelta(months=no)
                    com.append(valn)
                    print(no)
                self.env["account.move"].create(com)
            elif self.installment_no == '12':
                item = Command.create({
                        "name": prop.name,
                        'product_id': prop.property_type_id.product_id.id,
                        "quantity": 1.0,
                        "price_unit": price,
                    }),
                valn['invoice_line_ids'].append(item)
                com.append(vals1)
                for no in range(n):
                    vals1['invoice_date'] = date.today() + relativedelta(months=no)
                    com.append(valn)
                    print(no)
                self.env["account.move"].create(com)
            elif self.installment_no == '24':
                item = Command.create({
                        "name": prop.name,
                        'product_id': prop.property_type_id.product_id.id,
                        "quantity": 1.0,
                        "price_unit": price,
                    }),
                valn['invoice_line_ids'].append(item)
                com.append(vals1)
                for no in range(n):
                    vals1['invoice_date'] = date.today() + relativedelta(months=no)
                    com.append(valn)
                    print(no)
                self.env["account.move"].create(com)

            prop.action_sold()







