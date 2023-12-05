# -*- coding: utf-8 -*-

from odoo import models, Command
from odoo.exceptions import UserError, ValidationError


class EstateProperty(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "estate.property"

    # ------------------------------------------res config setting -------------------------------



    # ---------------------------------------- Action Methods -------------------------------------

    # def action_sold(self):
    #     res = super().action_sold()
    #
    #     return res
