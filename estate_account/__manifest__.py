# -*- coding: utf-8 -*-
{
    'name': "estate account",

    # any module necessary for this one to work correctly
    'depends': ['base', 'estate', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/installment_view.xml',
        'views/estate_property_inherit.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
