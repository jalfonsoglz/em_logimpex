# -*- coding: utf-8 -*-
{
    'name': "Logimpex - Extension Module",
    'summary': """Logimpex - Extension Module""",
    'description': """
    Logimpex - Extension Module
    """,
    'author': "Alfonso Gonzalez (alfonso@ptree.com.mx)",
    'website': "https://ptree.com.mx/",
    'category': 'Customizations',
    'version': '15.0.0.1.5',
    'license': "AGPL-3",
    'sequence': "-80",
    'depends': [
        'base',
        'mail',
        'account',
        'project',
        'sale_management',
    ],
    'data': [
        # Security
        'security/logimpex_security.xml',
        'security/ir.model.access.csv',
        # Imports
        'data/eml.seaports.airports.csv',
        'data/eml.buques.csv',
        # Reports
        'report/report.xml',
        'report/transferencia_form.xml',
        # Views
        'views/eml_expedientes.xml',
        'views/eml_operation_type.xml',
        'views/eml_containers_type.xml',
        'views/eml_borders.xml',
        'views/eml_buques.xml',
        'views/eml_seaports_airports.xml',
        'views/eml_containers.xml',
        'views/eml_transferencia.xml',
        'views/eml_docs.xml',
        'views/eml_docs_tags.xml',
        'views/project.project.xml',
        'views/account.move.xml',
        'views/res.partner.bank.xml',
        'views/res.partner.xml',
        # Data
        'data/eml_containers_type.xml',
        'data/eml_borders.xml',
        'data/eml_operation_type.xml',
        'data/eml_tags.xml',
        # Sequence
        'data/ir_sequence_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
