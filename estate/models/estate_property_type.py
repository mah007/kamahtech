from odoo import fields, models


class EstatePropertyType(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "sequence, name"

    