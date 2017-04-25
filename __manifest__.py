# -*- encoding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Bank Statements CSV Import',
    'category': 'Accounting & Finance',
    'summary': 'Import Bank Statements from CSV',
    'website': '',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Mick',
    'description': "",
    'data': [
        'views/account_csv.xml',
    ],
    'depends': [
        'account_bank_statement_import',
    ],
    'external_dependencies': {
        'python': [
            'unicodecsv',
            'chardet',
        ]
    },
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
}

