# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': """
        Odoo Real Estate
        """,

    'description': """
         Odoo Real Estate
    """,

    'author': "Kamatech",
    'website': "https://www.kamatech.com",
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/estate_property_offer_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        "views/res_users_views.xml",
        "views/estate_menus.xml",
        'reports/estate_template.xml',
        'reports/estate_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'sequence': 2,
}
