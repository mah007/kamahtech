# -*- coding: utf-8 -*-
{
    'name': "school",

    'summary': """
        School System""",

    'description': """
        school system for example
    """,

    'author': "Kamatech",
    'website': "https://www.kama.com",

    'category': 'school',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
