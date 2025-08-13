{
    'name': "Cinema App",
    'author': "mostafa abdelkareem",
    'category': "Media",
    'version': "17.0.0.1.0",
    'depends': ['base', 'sale_management', 'account', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu_view.xml',
        'views/cinema_view.xml',
        'views/crew_view.xml',
        'reports/movie_ticket.xml',
    ],
    'application': True,
}
