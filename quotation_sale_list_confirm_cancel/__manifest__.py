# -*- coding: utf-8 -*-

{
    'name': 'Sale/Quotation Confirm, Cancel, Set to Quotation, and Create Invoice from List View.',
    'version': '16.0.0.0.0',
    'category': 'Sales/Sales',
    'license': 'LGPL-3',
    'summary': """Confirm, Cancel, Set to Quotation, and Create Invoice your Sale/Quotation from list views""",
    'depends': [
        'base',
        'sale',
    ],
    'author': 'Naing Lynn Htun',
    'support': 'konainglynnhtun@gmail.com',
    'description': """
    - Confirm, Cancel and Set to Quotation, Quotation from list view
    - Create Invoice and Set to Quotation, Sale from list view
    """,
    'data': [
        'views/sale.xml',
    ],
    'license': 'AGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
