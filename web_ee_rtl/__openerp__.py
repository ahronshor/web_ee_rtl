# -*- coding: utf-8 -*-
{
    'name': "Web EE RTL",

    'summary': """
        Support RTL for Arabic, Hebrew and Persian UI.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mohamed Magdy",
    'website': "http://morepython.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Web',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'web_enterprise', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/res.lang.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
