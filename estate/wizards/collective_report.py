# wizard

# -*- coding: utf-8 -*-
# Part of Odoo. Tutorials.

from odoo import fields, models, _
from odoo.exceptions import UserError, ValidationError

class EstateReports(models.TransientModel):
    _name = 'estate.property.reports'
    _description = "Reports for property"

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",

    )
    date = fields.Date('Date')

    def print_property_report(self):

        domain = []
        if self.property_type_id:
            domain.append(('property_type_id', '=', self.property_type_id.id))
        if self.state:
            domain.append(('state', '=', self.state))
        if self.date:
            domain.append(('date_availability', '=', self.date))
        print(domain)
        props = self.env['estate.property'].sudo().search_read(domain)

        data = {

            'form': self.read()[0],
            'props': props,
        }
        return self.env.ref('estate.action_report_estate_collective').report_action(self, data=data)
