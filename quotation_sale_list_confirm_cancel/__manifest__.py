# -*- coding: utf-8 -*-
{
    'name': "Sale/Quotation Confirm, Cancel, Set to Quotation, and Create Invoice from List View.",

    'summary': """
        Confirm, Cancel, Set to Quotation, and Create Invoice your Sale/Quotation from list views""",

    'description': """
        - Confirm, Cancel and Set to Quotation, Quotation from list view
        - Create Invoice and Set to Quotation, Sale from list view
    """,

    'author': "Naing Lynn Htun",
    'support': 'konainglynnhtun@gmail.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],
    'support': 'konainglynnhtun@gmail.com',
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale.xml',
    ],
    'license': 'AGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
