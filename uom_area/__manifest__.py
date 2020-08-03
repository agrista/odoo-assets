# -*- coding: utf-8 -*-
{
    'name': "Area UoM",
    'summary': """
        Add area units of measure
        """,
    'description': """
        Add area to units of measure
    """,
    'author': "Agrista",
    'website': "http://agrista.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['uom'],

    # always loaded
    'data': [
        'data/uom_area_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
