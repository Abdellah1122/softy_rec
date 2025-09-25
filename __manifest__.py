{
    'name': 'Softy Recruitment',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Extension for Odoo Recruitment Module',
    'description': """
        Softy Recrutement
    """,
    'license': 'LGPL-3',
    'depends': [
        'base',
        'hr_recruitment',
        'hr',
    ],
    'data': [
         'security/ir.model.access.csv',
         'data/mails.xml',
         'views/menu_views..xml',
         'views/doc_views.xml',
         'views/candidate_views.xml',
         'views/jobs.xml',
         'views/candidature_views.xml',
         
        
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 100,
}