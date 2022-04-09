# -*- coding: utf-8 -*-
{
    'name': "Extension Module Logimpex",
    'summary': """Extension Module Logimpex""",
    'description': """
    Extension Module Logimpex
    """,
    'author': "Alfonso Gonzalez (alfonso@ptree.com.mx)",
    'website': "https://ptree.com.mx/",
    'category': 'Customizations',
    'version': '15.0.0.0.1',
    'license': "AGPL-3",
    'sequence': "-100",
    'depends': [
        'base',
        'mail',
        'account'
    ],
    'data': [
        # Security
        'security/logimpex_security.xml',
        'security/ir.model.access.csv',
        # Views
        'views/eml_expedientes.xml',
        'views/eml_operation_type.xml',
        'views/eml_containers_type.xml',
        'views/eml_borders.xml',
        'views/eml_seaports_airports.xml',
        'views/eml_containers.xml',
        # Data
        'data/eml_containers_type.xml',
        'data/eml_borders.xml',
        'data/eml_operation_type.xml',
        'data/eml_seaports_airports.xml',
        # Sequence
        'data/ir_sequence_data.xml'
        # Reports
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}