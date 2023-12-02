# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'school.school'

    name = fields.Char('Student name')
    dob = fields.Date('Date Of birth')
    age = fields.Integer('Age',compute='_compute_age')
    description = fields.Text('Info')

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                rec.age = int(date.today().year - rec.dob.year)
            else:
                rec.age = 0
