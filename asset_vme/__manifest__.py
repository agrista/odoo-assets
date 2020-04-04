# -*- coding: utf-8 -*-
{
    'name': "VMW Assets",

    'summary': """
        Management of vehicles,machinery, and equipment in a agricultural context
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Agrista GmbH",
    'website': "http://agrista.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Assets',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/stock_data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
